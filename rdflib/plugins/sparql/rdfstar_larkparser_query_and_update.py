# sparqlbytes_processing = "PREFIX rdf:       <http://www.rdf/example/> \n PREFIX :       <http://example/> \n SELECT * {<<:a :b :c>> ?p ?o}"

import re
from xml.etree.ElementPath import prepare_predicate
import lark
import hashlib
from lark import (
    Lark,
    Transformer,
    Tree,
)
from lark.visitors import Visitor
from lark.reconstruct import Reconstructor

from lark.lexer import (
    Token,
)

from typing import List, Dict, Union, Callable, Iterable, Optional

from lark import Lark
from lark.tree import Tree, ParseTree
from lark.visitors import Transformer_InPlace
from lark.lexer import Token, PatternStr, TerminalDef
from lark.grammar import Terminal, NonTerminal, Symbol

from lark.tree_matcher import TreeMatcher, is_discarded_terminal
from lark.utils import is_id_continue

from rdflib.term import RdfstarTriple

def myHash(text:str):
  return str(hashlib.md5(text.encode('utf-8')).hexdigest())

grammar = r"""sparqlrequest: request
    request: queryunit | updateunit
    queryunit: query
    query: prologue ( selectquery | constructquery | describequery | askquery ) valuesclause
    updateunit	  :  	update
    prologue	  :  	( basedecl | prefixdecl )*
    basedecl	  :  	"BASE" IRIREF
    prefixdecl	  :  	"PREFIX" PNAME_NS IRIREF
    selectquery	  :  	selectclause datasetclause* whereclause solutionmodifier
    subselect	  :  	selectclause whereclause solutionmodifier valuesclause
    selectclause	  :  	"SELECT" ( "DISTINCT" | "REDUCED" )? ( ( var | ( "(" expression "AS" var ")" ) )+ | "*" )
    constructquery	  :  	"CONSTRUCT" ( constructtemplate datasetclause* whereclause solutionmodifier | datasetclause* "WHERE" "{" triplestemplate? "}" solutionmodifier )
    describequery	  :  	"DESCRIBE" ( varoriri+ | "*" ) datasetclause* whereclause? solutionmodifier
    askquery	  :  	"ASK" datasetclause* whereclause solutionmodifier
    datasetclause	  :  	"FROM" ( defaultgraphclause | namedgraphclause )
    defaultgraphclause	  :  	sourceselector
    namedgraphclause	  :  	"NAMED" sourceselector
    sourceselector	  :  	iri
    whereclause	  :  	"WHERE"? groupgraphpattern
    solutionmodifier	  :  	groupclause? havingclause? orderclause? limitoffsetclauses?
    groupclause	  :  	"GROUP" "BY" groupcondition+
    groupcondition	  :  	builtincall | functioncall | "(" expression ( "AS" var )? ")" | var
    havingclause	  :  	"HAVING" havingcondition+
    havingcondition	  :  	constraint
    orderclause	  :  	"ORDER" "BY" ordercondition+
    ordercondition	  :  	( ( "ASC" | "DESC" ) brackettedexpression )
    | ( constraint | var )
    limitoffsetclauses	  :  	limitclause offsetclause? | offsetclause limitclause?
    limitclause	  :  	"LIMIT" integer
    offsetclause	  :  	"OFFSET" integer
    valuesclause	  :  	( "VALUES" datablock )?
    update	  :  	prologue ( update1 ( ";" update )? )?
    update1	  :  	load | clear | drop | add | move | copy | create | insertdata | deletedata | deletewhere | modify
    load	  :  	"load" "SILENT"? iri ( "INTO" graphref )?
    clear	  :  	"clear" "SILENT"? graphrefall
    drop	  :  	"drop" "SILENT"? graphrefall
    create	  :  	"create" "SILENT"? graphref
    add	  :  	"add" "SILENT"? graphordefault "TO" graphordefault
    move	  :  	"move" "SILENT"? graphordefault "TO" graphordefault
    copy	  :  	"copy" "SILENT"? graphordefault "TO" graphordefault
    insertdata	  :  	"INSERT DATA" quaddata
    deletedata	  :  	"DELETE DATA" quaddata
    deletewhere	  :  	"DELETE WHERE" quadpattern
    modify	  :  	( "WITH" iri )? ( deleteclause insertclause? | insertclause ) usingclause* "WHERE" groupgraphpattern
    deleteclause	  :  	"DELETE" quadpattern
    insertclause	  :  	"INSERT" quadpattern
    usingclause	  :  	"USING" ( iri | "NAMED" iri )
    graphordefault	  :  	"DEFAULT" | "GRAPH"? iri
    graphref	  :  	"GRAPH" iri
    graphrefall	  :  	graphref | "DEFAULT" | "NAMED" | "ALL"
    quadpattern	  :  	"{" quads "}"
    quaddata	  :  	"{" quads "}"
    quads	  :  	triplestemplate? ( quadsnottriples "."? triplestemplate? )*
    quadsnottriples	  :  	"GRAPH" varoriri "{" triplestemplate? "}"
    triplestemplate	  :  	triplessamesubject ( "." triplestemplate? )?
    groupgraphpattern	  :  	"{" ( subselect | groupgraphpatternsub ) "}"
    groupgraphpatternsub	  :  	triplesblock? ( graphpatternnottriples "."? triplesblock? )*
    triplesblock	  :  	triplessamesubjectpath ( "." triplesblock? )?
    graphpatternnottriples	  :  	grouporuniongraphpattern | optionalgraphpattern | minusgraphpattern | graphgraphpattern | servicegraphpattern | filter | bind | inlinedata
    optionalgraphpattern	  :  	"OPTIONAL" groupgraphpattern
    graphgraphpattern	  :  	"GRAPH" varoriri groupgraphpattern
    servicegraphpattern	  :  	"SERVICE" "SILENT"? varoriri groupgraphpattern
    bind	  :  	"bind" "(" expression "AS" var ")"
    inlinedata	  :  	"VALUES" datablock
    datablock	  :  	inlinedataonevar | inlinedatafull
    inlinedataonevar	  :  	var "{" datablockvalue* "}"
    inlinedatafull	  :  	( NIL | "(" var* ")" ) "{" ( "(" datablockvalue* ")" | NIL )* "}"
    datablockvalue	  :  	quotedtriple | iri | rdfliteral | numericliteral | booleanliteral | "UNDEF"
    minusgraphpattern	  :  	"MINUS" groupgraphpattern
    grouporuniongraphpattern	  :  	groupgraphpattern ( "UNION" groupgraphpattern )*
    filter	  :  	"filter" constraint
    constraint	  :  	brackettedexpression | builtincall | functioncall
    functioncall	  :  	iri arglist
    arglist	  :  	NIL | "(" "DISTINCT"? expression ( "," expression )* ")"
    expressionlist	  :  	NIL | "(" expression ( "," expression )* ")"
    constructtemplate	  :  	"{" constructtriples? "}"
    constructtriples	  :  	triplessamesubject ( "." constructtriples? )?
    triplessamesubject	  :  	varortermorquotedtp propertylistnotempty | triplesnode propertylist
    propertylist	  :  	propertylistnotempty?
    propertylistnotempty	  :  	verb objectlist ( ";" ( verb objectlist )? )*
    verb	  :  	varoriri | "a"
    objectlist	  :  	object ( "," object )*
    object	  :  	graphnode annotationpattern?
    triplessamesubjectpath	  :  	varortermorquotedtp propertylistpathnotempty | triplesnodepath propertylistpath
    propertylistpath	  :  	propertylistpathnotempty?
    propertylistpathnotempty	  :  	( verbpath | verbsimple ) objectlistpath ( ";" ( ( verbpath | verbsimple ) objectlist )? )*
    verbpath	  :  	path
    verbsimple	  :  	var
    objectlistpath	  :  	objectpath ( "," objectpath )*
    objectpath	  :  	graphnodepath annotationpattern?
    path	  :  	pathalternative
    pathalternative	  :  	pathsequence ( "|" pathsequence )*
    pathsequence	  :  	patheltorinverse ( "/" patheltorinverse )*
    pathelt	  :  	pathprimary pathmod?
    patheltorinverse	  :  	pathelt | "^" pathelt
    pathmod	  :  	"?" | "*" | "+"
    pathprimary	  :  	iri | "a" | "!" pathnegatedpropertyset | "(" path ")"
    pathnegatedpropertyset	  :  	pathoneinpropertyset | "(" ( pathoneinpropertyset ( "|" pathoneinpropertyset )* )? ")"
    pathoneinpropertyset	  :  	iri | "a" | "^" ( iri | "a" )
    integer	  :  	INTEGER
    triplesnode	  :  	collection | blanknodepropertylist
    blanknodepropertylist	  :  	"[" propertylistnotempty "]"
    triplesnodepath	  :  	collectionpath | blanknodepropertylistpath
    blanknodepropertylistpath	  :  	"[" propertylistpathnotempty "]"
    collection	  :  	"(" graphnode+ ")"
    collectionpath	  :  	"(" graphnodepath+ ")"
    graphnode	  :  	varortermorquotedtp | triplesnode
    graphnodepath	  :  	varortermorquotedtp | triplesnodepath
    varorterm	  :  	var | graphterm
    varoriri	  :  	var | iri
    var	  :  	var1 | var2
    graphterm	  :  	iri | rdfliteral | numericliteral | booleanliteral | blanknode | NIL
    expression	  :  	conditionalorexpression
    conditionalorexpression	  :  	conditionalandexpression ( "||" conditionalandexpression )*
    conditionalandexpression	  :  	valuelogical ( "&&" valuelogical )*
    valuelogical	  :  	relationalexpression
    relationalexpression	  :  	numericexpression ( "=" numericexpression | "!=" numericexpression | "<" numericexpression | ">" numericexpression | "<=" numericexpression | ">=" numericexpression | "IN" expressionlist | "NOT" "IN" expressionlist )?
    numericexpression	  :  	additiveexpression
    additiveexpression	  :  	multiplicativeexpression ( "+" multiplicativeexpression | "-" multiplicativeexpression | ( numericliteralpositive | numericliteralnegative ) ( ( "*" unaryexpression ) | ( "/" unaryexpression ) )* )*
    multiplicativeexpression	  :  	unaryexpression ( "*" unaryexpression | "/" unaryexpression )*
    unaryexpression	  :  	  "!" primaryexpression
    | "+" primaryexpression
    | "-" primaryexpression
    | primaryexpression
    primaryexpression	  :  	brackettedexpression | builtincall | iriorfunction | rdfliteral | numericliteral | booleanliteral | var | exprquotedtp
    brackettedexpression	  :  	"(" expression ")"
    builtincall	  :  	  aggregate
    | "STR" "(" expression ")"
    | "LANG" "(" expression ")"
    | "LANGMATCHES" "(" expression "," expression ")"
    | "DATATYPE" "(" expression ")"
    | "BOUND" "(" var ")"
    | "IRI" "(" expression ")"
    | "URI" "(" expression ")"
    | "BNODE" ( "(" expression ")" | NIL )
    | "RAND" NIL
    | "ABS" "(" expression ")"
    | "CEIL" "(" expression ")"
    | "FLOOR" "(" expression ")"
    | "ROUND" "(" expression ")"
    | "CONCAT" expressionlist
    | substringexpression
    | "STRLEN" "(" expression ")"
    | strreplaceexpression
    | "UCASE" "(" expression ")"
    | "LCASE" "(" expression ")"
    | "ENCODE_FOR_URI" "(" expression ")"
    | "CONTAINS" "(" expression "," expression ")"
    | "STRSTARTS" "(" expression "," expression ")"
    | "STRENDS" "(" expression "," expression ")"
    | "STRBEFORE" "(" expression "," expression ")"
    | "STRAFTER" "(" expression "," expression ")"
    | "YEAR" "(" expression ")"
    | "MONTH" "(" expression ")"
    | "DAY" "(" expression ")"
    | "HOURS" "(" expression ")"
    | "MINUTES" "(" expression ")"
    | "SECONDS" "(" expression ")"
    | "TIMEZONE" "(" expression ")"
    | "TZ" "(" expression ")"
    | "NOW" NIL
    | "UUID" NIL
    | "STRUUID" NIL
    | "MD5" "(" expression ")"
    | "SHA1" "(" expression ")"
    | "SHA256" "(" expression ")"
    | "SHA384" "(" expression ")"
    | "SHA512" "(" expression ")"
    | "COALESCE" expressionlist
    | "IF" "(" expression "," expression "," expression ")"
    | "STRLANG" "(" expression "," expression ")"
    | "STRDT" "(" expression "," expression ")"
    | "sameTerm" "(" expression "," expression ")"
    | "isIRI" "(" expression ")"
    | "isURI" "(" expression ")"
    | "isBLANK" "(" expression ")"
    | "isLITERAL" "(" expression ")"
    | "isNUMERIC" "(" expression ")"
    | regexexpression
    | existsfunc
    | notexistsfunc
    | "TRIPLE" "(" expression "," expression "," expression ")"
    | "SUBJECT" "(" expression ")"
    | "PREDICATE" "(" expression ")"
    | "OBJECT" "(" expression ")"
    | "isTRIPLE" "(" expression ")"
    quotedtp	: "<<" qtsubjectorobject verb qtsubjectorobject ">>"
    quotedtriple	: "<<" datavalueterm ( iri | "a" ) datavalueterm ">>"
    qtsubjectorobject	: var | blanknode | iri | rdfliteral | numericliteral | booleanliteral | quotedtp
    datavalueterm	: iri | rdfliteral | numericliteral | booleanliteral | quotedtriple
    varortermorquotedtp	: var | graphterm | quotedtp
    annotationpattern	: "{|" propertylistnotempty "|}"
    annotationpatternpath	: "{|" propertylistpathnotempty "|}"
    exprquotedtp	: "<<" exprvarorterm verb exprvarorterm ">>"
    exprvarorterm	: iri | rdfliteral | numericliteral | booleanliteral | var | exprquotedtp
    regexexpression	  :  	"REGEX" "(" expression "," expression ( "," expression )? ")"
    substringexpression	  :  	"SUBSTR" "(" expression "," expression ( "," expression )? ")"
    strreplaceexpression	  :  	"REPLACE" "(" expression "," expression "," expression ( "," expression )? ")"
    existsfunc	  :  	"EXISTS" groupgraphpattern
    notexistsfunc	  :  	"NOT" "EXISTS" groupgraphpattern
    aggregate	  :  	  "COUNT" "(" "DISTINCT"? ( "*" | expression ) ")"
    | "SUM" "(" "DISTINCT"? expression ")"
    | "MIN" "(" "DISTINCT"? expression ")"
    | "MAX" "(" "DISTINCT"? expression ")"
    | "AVG" "(" "DISTINCT"? expression ")"
    | "SAMPLE" "(" "DISTINCT"? expression ")"
    | "GROUP_CONCAT" "(" "DISTINCT"? expression ( ";" "SEPARATOR" "=" string )? ")"
    iriorfunction	  :  	iri arglist?
    rdfliteral	  :  	string ( LANGTAG | ( "^^" iri ) )?
    numericliteral	  :  	numericliteralunsigned | numericliteralpositive | numericliteralnegative
    numericliteralunsigned	  :  	INTEGER | DECIMAL | DOUBLE
    numericliteralpositive	  :  	INTEGER_POSITIVE | DECIMAL_POSITIVE | DOUBLE_POSITIVE
    numericliteralnegative	  :  	INTEGER_NEGATIVE | DECIMAL_NEGATIVE | DOUBLE_NEGATIVE
    booleanliteral	  :  	"true" | "false"
    string	  :  	STRING_LITERAL_QUOTE | STRING_LITERAL_SINGLE_QUOTE | STRING_LITERAL_LONG_QUOTE | STRING_LITERAL_LONG_SINGLE_QUOTE
    iri	  :  	IRIREF | prefixedname
    prefixedname	  :  	PNAME_LN | PNAME_NS
    blanknode	  :  	BLANK_NODE_LABEL | ANON

    BASE_DIRECTIVE: "@base"
    var1	  : 	"?" varname
    var2	  : 	"$" varname
    varname	  : 	PN_CHARS
    IRIREF: "<" (/[^\x00-\x20<>"{}|^`\\]/ | UCHAR)* ">"
    PNAME_NS: PN_PREFIX? ":"
    PNAME_LN: PNAME_NS PN_LOCAL
    BLANK_NODE_LABEL: "_:" (PN_CHARS_U | /[0-9]/) ((PN_CHARS | ".")* PN_CHARS)?
    LANGTAG: "@" /[a-zA-Z]+/ ("-" /[a-zA-Z0-9]+/)*
    INTEGER: /[+-]?[0-9]+/
    NIL	  :  	"(" WS* ")"
    DECIMAL: /[+-]?[0-9]*/ "." /[0-9]+/
    DOUBLE: /[+-]?/ (/[0-9]+/ "." /[0-9]*/ EXPONENT
        | "." /[0-9]+/ EXPONENT | /[0-9]+/ EXPONENT)
    INTEGER_POSITIVE	  :  	"+" INTEGER
    DECIMAL_POSITIVE	  :  	"+" DECIMAL
    DOUBLE_POSITIVE	      :  	"+" DOUBLE
    INTEGER_NEGATIVE	  :  	"-" INTEGER
    DECIMAL_NEGATIVE	  :	    "-" DECIMAL
    DOUBLE_NEGATIVE	      :	    "-" DOUBLE
    EXPONENT: /[eE][+-]?[0-9]+/
    STRING_LITERAL_QUOTE: "\"" (/[^\x22\x5C\x0A\x0D]/ | ECHAR | UCHAR)* "\""
    STRING_LITERAL_SINGLE_QUOTE: "'" (/[^\x27\x5C\x0A\x0D]/ | ECHAR | UCHAR)* "'"
    STRING_LITERAL_LONG_SINGLE_QUOTE: "'''" (/'|''/? (/[^'\\]/ | ECHAR | UCHAR))* "'''"
    STRING_LITERAL_LONG_QUOTE: "\"\"\"" (/"|""/? (/[^"\\]/ | ECHAR | UCHAR))* "\"\"\""
    UCHAR: "\\u" HEX~4 | "\\U" HEX~8
    ECHAR: "\\" /[tbnrf"'\\]/
    WS: /[\x20\x09\x0D\x0A]/
    ANON: "[" WS* "]"
    PN_CHARS_BASE: /[A-Za-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD\U00010000-\U000EFFFF]/
    PN_CHARS_U: PN_CHARS_BASE | "_"
    PN_CHARS: PN_CHARS_U | /[\-0-9\u00B7\u0300-\u036F\u203F-\u2040]/
    PN_PREFIX: PN_CHARS_BASE ((PN_CHARS | ".")* PN_CHARS)?
    PN_LOCAL: (PN_CHARS_U | ":" | /[0-9]/ | PLX) ((PN_CHARS | "." | ":" | PLX)* (PN_CHARS | ":" | PLX))?
    PLX: PERCENT | PN_LOCAL_ESC
    PERCENT: "%" HEX~2
    HEX: /[0-9A-Fa-f]/
    PN_LOCAL_ESC: "\\" /[_~\.\-!$&'()*+,;=\/?#@%]/

    %ignore WS
    COMMENT: "#" /[^\n]/*
    %ignore COMMENT
    """

quoted_triple_dictionary = dict()
triples_dictionary = dict()
def is_iter_empty(i):
    try:
        _ = next(i)
        return False
    except StopIteration:
        return True

class WriteTokensTransformer(Transformer_InPlace):
    "Inserts discarded tokens into their correct place, according to the rules of grammar"

    tokens: Dict[str, TerminalDef]
    term_subs: Dict[str, Callable[[Symbol], str]]

    def __init__(self, tokens: Dict[str, TerminalDef], term_subs: Dict[str, Callable[[Symbol], str]]) -> None:
        self.tokens = tokens
        self.term_subs = term_subs

    def __default__(self, data, children, meta):
        if not getattr(meta, 'match_tree', False):
            return Tree(data, children)

        iter_args = iter(children)
        to_write = []
        for sym in meta.orig_expansion:
            if is_discarded_terminal(sym):
                try:
                    v = self.term_subs[sym.name](sym)
                except KeyError:
                    t = self.tokens[sym.name]
                    if not isinstance(t.pattern, PatternStr):
                        raise NotImplementedError("Reconstructing regexps not supported yet: %s" % t)

                    v = t.pattern.value
                to_write.append(v)
            else:
                x = next(iter_args)
                if isinstance(x, list):
                    to_write += x
                else:
                    if isinstance(x, Token):
                        assert Terminal(x.type) == sym, x
                    else:
                        assert NonTerminal(x.data) == sym, (sym, x)
                    to_write.append(x)

        assert is_iter_empty(iter_args)
        return to_write

class Reconstructorv2(TreeMatcher):
    """
    A Reconstructor that will, given a full parse Tree, generate source code.
    Note:
        The reconstructor cannot generate values from regexps. If you need to produce discarded
        regexes, such as newlines, use `term_subs` and provide default values for them.
    Paramters:
        parser: a Lark instance
        term_subs: a dictionary of [Terminal name as str] to [output text as str]
    """

    write_tokens: WriteTokensTransformer

    def __init__(self, parser: Lark, term_subs: Optional[Dict[str, Callable[[Symbol], str]]]=None) -> None:
        TreeMatcher.__init__(self, parser)

        self.write_tokens = WriteTokensTransformer({t.name:t for t in self.tokens}, term_subs or {})

    def _reconstruct(self, tree):
        unreduced_tree = self.match_tree(tree, tree.data)

        res = self.write_tokens.transform(unreduced_tree)
        for item in res:
            if isinstance(item, Tree):
                # TODO use orig_expansion.rulename to support templates
                yield from self._reconstruct(item)
            else:
                yield item

    def reconstruct(self, tree: ParseTree, postproc: Optional[Callable[[Iterable[str]], Iterable[str]]]=None, insert_spaces: bool=True) -> str:
        x = self._reconstruct(tree)
        if postproc:
            x = postproc(x)
        y = []
        prev_item = ''
        for item in x:
            if insert_spaces and prev_item and item and is_id_continue(prev_item[-1]) and is_id_continue(item[0]):
                y.append(' ')
            y.append(item)
            prev_item = item
        return ' '.join(y)

# sparql_lark = Lark(grammar, start="queryunit", parser="lalr", maybe_placeholders=False)

# from lark import Visitor, v_args

# tree = sparql_lark.parse(query)
quotation_dict = []
quotationreif = []
prefix_dictionary = dict()
annotation_s_p_o = []
to_remove = []
annotation_dict = dict()
output = ""
def Parsing_and_processing_updates(query):
    global output, annotation_dict,annotation_s_p_o, to_remove, grammar

    sparql_lark = Lark(grammar, start="update", parser="lalr", maybe_placeholders=False)

    from lark import Visitor, v_args
    print("query", query)
    tree = sparql_lark.parse(query)
    print("tree", tree)
    quotation_dict = []
    quotationreif = []
    prefix_dictionary = dict()
    annotation_s_p_o = []
    # to_remove = []
    to_remove = dict()
    annotation_dict = dict()
    output = ""
    def myHash(text:str):
        return str(hashlib.md5(text.encode('utf-8')).hexdigest())
    prefix_replace_list = []

    class Expandanotation(Visitor):

        # global annotation_s_p_o, to_remove, output
        def __init__(self):
            super().__init__()
            self.variable_list = []

        def triplessamesubject(self, var):
            tri = Reconstructor(sparql_lark).reconstruct(var)
            if "{|" in tri:
                print("twsetstse", annotation_dict)
                print(Reconstructor(sparql_lark).reconstruct(var.children[0]), "\nasdasdas", Reconstructor(sparql_lark).reconstruct(var.children[1]))
                # if len(var.children[0].children) == 2:
                # var.children[0] =
                predicate_object_list2 = var.children[1]
                subject = Reconstructor(sparql_lark).reconstruct(var.children[0])
                print("subject",subject )
                po_list = []
                predicate_objects = predicate_object_list2.children
                for x in range(0, len(predicate_objects)):

                    predicate_or_object = Reconstructor(sparql_lark).reconstruct(predicate_objects[x])
                    po_list.append(predicate_or_object)

                    if len(po_list) == 2:
                        if "," in po_list[1]:
                            po_lists = po_list[1].split(",")

                            for y in po_lists:

                                try:
                                    object_annotation = y.split("{|",1)
                                    o1 = object_annotation[0]
                                    a1 = "{|"+object_annotation[1]
                                    a1 = a1.strip()
                                    a1_Dict = annotation_dict[a1]
                                    spo_list = [subject,po_list[0],o1, a1_Dict]

                                    annotation_s_p_o.append(spo_list)
                                except:
                                    spo_list = [subject,po_list[0],y]
                                    annotation_s_p_o.append(spo_list)
                        else:
                            object_annotation = po_list[1].split("{|",1)
                            o1 = object_annotation[0]
                            a1 = "{|"+object_annotation[1]
                            a1_Dict = annotation_dict[a1]
                            spo_list = [subject, po_list[0], o1, a1_Dict]
                            annotation_s_p_o.append(spo_list)
                        po_list = []
                if not tri in to_remove:
                    to_remove[tri] = spo_list

        def triplessamesubjectpath(self, var):
            tri = Reconstructor(sparql_lark).reconstruct(var)
            if "{|" in tri:
                print("tblock", annotation_dict)
                print(var.children[0],Reconstructor(sparql_lark).reconstruct(var.children[0]), "\nasdasdas")#
                # if len(var.children[0].children) == 2:
                # var.children[0] =
                predicate_object_list2 = var.children[1]
                subject = Reconstructor(sparql_lark).reconstruct(var.children[0])
                print("subject",subject )
                po_list = []
                predicate_objects = predicate_object_list2.children
                for x in range(0, len(predicate_objects)):

                    predicate_or_object = Reconstructor(sparql_lark).reconstruct(predicate_objects[x])
                    po_list.append(predicate_or_object)

                    if len(po_list) == 2:
                        if "," in po_list[1]:
                            po_lists = po_list[1].split(",")

                            for y in po_lists:

                                try:
                                    object_annotation = y.split("{|",1)
                                    o1 = object_annotation[0]
                                    a1 = "{|"+object_annotation[1]
                                    a1 = a1.strip()
                                    a1_Dict = annotation_dict[a1]
                                    spo_list = [subject,po_list[0],o1, a1_Dict]

                                    annotation_s_p_o.append(spo_list)
                                except:
                                    spo_list = [subject,po_list[0],y]
                                    annotation_s_p_o.append(spo_list)
                        else:
                            object_annotation = po_list[1].split("{|",1)
                            o1 = object_annotation[0]
                            a1 = "{|"+object_annotation[1]
                            a1_Dict = annotation_dict[a1]
                            spo_list = [subject, po_list[0], o1, a1_Dict]
                            annotation_s_p_o.append(spo_list)
                        po_list = []
                if not tri in to_remove:
                    to_remove[tri] = spo_list

        def annotationpattern(self, var):
            appends1 = []
            tri2 = Reconstructor(sparql_lark).reconstruct(var)
            for x in var.children[0].children:
                test = Reconstructor(sparql_lark).reconstruct(x)
                print("test", test)
                if "{|" in test:
                    test123 = test.split("{|",1)
                    object = test123[0]
                    test123.pop(0)
                    test_annotation = "{|"+ "".join(test123)
                    result = annotation_dict[test_annotation]
                    appends1.append(object)
                    appends1.append(result)
                else:
                    appends1.append(test)
            if not tri2 in annotation_dict:
                annotation_dict[tri2] = appends1
            elif not appends1 == annotation_dict[tri2]:
                for x in appends1:
                    annotation_dict[tri2].append(x)

    class ExpandPrefix(Visitor):
        def __init__(self):
            super().__init__()
            self.variable_list = []

        def iri(self, children):
            # print(":iri:", children)
            try:
                prefix_replace_list.append((children.children[0]).children[0])
            except:#
                # no prefix
                pass

        def prefixdecl(self, children):
            vr = Reconstructor(sparql_lark).reconstruct(children)
            prefix_dictionary[str(children.children[0])] = str(children.children[1])
            self = Tree(Token('RULE', 'prefixdecl'), [])

        def base(self, children):
            base_directive, base_iriref = children
            if base_directive.startswith('@') and base_directive != '@base':
                raise ValueError('Unexpected @base: ' + base_directive)

    # class Process_update(Visitor):
    #     global quoted_triple_dictionary, triples_dictionary
    #     def __init__(self):
    #         super().__init__()
    #         self.variable_list = []

    #     def quotedtp(self, var):
    #         vr = Reconstructorv2(sparql_lark).reconstruct(var) # can shift to var matching, temporarily debuging using reconstruct
    #         # print("quoted triple:", vr)
    #         # print("varchildren", var.children)
    #         subject = var.children[0]
    #         predicate = var.children[1]
    #         object = var.children[2]

    #         subject = Reconstructorv2(sparql_lark).reconstruct(subject)
    #         predicate = Reconstructorv2(sparql_lark).reconstruct(predicate)
    #         object = Reconstructorv2(sparql_lark).reconstruct(object)

    #         # print("spo",subject,predicate,object)
    #         if subject in quoted_triple_dictionary:
    #             subject = quoted_triple_dictionary[subject]

    #         if predicate in quoted_triple_dictionary:
    #             predicate = quoted_triple_dictionary[predicate]

    #         if object in quoted_triple_dictionary:
    #             object = quoted_triple_dictionary[object]

    #         if not vr in quoted_triple_dictionary:
    #             rdfstartriple = RdfstarTriple(myHash(vr))
    #             rdfstartriple.setSubject(subject)
    #             rdfstartriple.setPredicate(predicate)
    #             rdfstartriple.setObject(object)
    #             quoted_triple_dictionary[vr] = rdfstartriple

    #     def triplessamesubject(self, var):
    #         vr = Reconstructorv2(sparql_lark).reconstruct(var) # can shift to var matching, temporarily debuging using reconstruct
    #         # print("triplessamesubject", Reconstructorv2(sparql_lark).reconstruct(var.children[0]), "\n",Reconstructorv2(sparql_lark).reconstruct(var.children[1]))
    #         subject = var.children[0]
    #         predicate = var.children[1].children[0]
    #         object = var.children[1].children[1]

    #         subject = Reconstructorv2(sparql_lark).reconstruct(subject)
    #         predicate = Reconstructorv2(sparql_lark).reconstruct(predicate)
    #         object = Reconstructorv2(sparql_lark).reconstruct(object)
    #         print("spo",subject,predicate,object)
    #         if subject in quoted_triple_dictionary:
    #             subject = quoted_triple_dictionary[subject]

    #         if predicate in quoted_triple_dictionary:
    #             predicate = quoted_triple_dictionary[predicate]

    #         if object in quoted_triple_dictionary:
    #             object = quoted_triple_dictionary[object]

    #         if not vr in triples_dictionary:
    #             triples_dictionary[vr] = (subject, predicate, object)

    #         # triples_dictionary
    #     def insertdata(self, var):

    #         vr = Reconstructorv2(sparql_lark).reconstruct(var.children[0].children[0])

    #         for x in var.children[0].children[0]:
    #             vr = Reconstructorv2(sparql_lark).reconstruct(x)
    #             if x in triples_dictionary:

    #         print("dictionary", quoted_triple_dictionary, triples_dictionary)
    #         print("insert: ", self, var, var.children)

    at = ExpandPrefix().visit(tree)
    sparql = Reconstructor(sparql_lark).reconstruct(tree)
    for z in prefix_dictionary:
        replace = "PREFIX" + z + prefix_dictionary[z]
        replace1 = "PREFIX" + " "+ z + prefix_dictionary[z]
        replace2 = "PREFIX" + z + " " +prefix_dictionary[z]
        replace3 = "PREFIX" +" "+ z+ " " + prefix_dictionary[z]
        sparql = sparql.replace(replace, "")
        sparql = sparql.replace(replace1, "")
        sparql = sparql.replace(replace2, "")
        sparql = sparql.replace(replace3, "")
        pd = prefix_dictionary[z].strip("<")
        pd = pd.strip(">")
        for y in prefix_replace_list:
            if z in y:
                newy = y.replace(z, pd) #repalce y
                newy = "<" + newy + ">"
                # print("newy", newy)
                sparql = sparql.replace(y, newy)
            else:
                pass
    tree = sparql_lark.parse(sparql)
    tt = Expandanotation().visit(tree)

    tree_after = Reconstructor(sparql_lark).reconstruct(tree)
    print("asdasdasdasdas", to_remove, annotation_s_p_o)
    splittree_after = tree_after.split(">")

    PREFIX_substitute = dict()
    for x in splittree_after:

        if "PREFIX" in x:
            y = x + ">"+" " + "\n"
            PREFIX_substitute[x+">"] = y
    for z in PREFIX_substitute:
        tree_after = tree_after.replace(z, "")
    for z in PREFIX_substitute:
        tree_after =  PREFIX_substitute[z] + tree_after


    if "PREFIX:" in tree_after:
        tree_after = tree_after.replace("PREFIX:", "PREFIX :")

    def expand_to_rdfstar(x):
        global output
        spo = "<<"+x[0] +" "+x[1] + " " + x[2]+">>"
        if len(x[3]) == 2:
            output += spo + " "+ str(x[3][0]) +" "+str(x[3][1])  + "\n"
        elif len(x[3]) == 3:
            output += spo + " "+ x[3][0] +" "+x[3][1]  + "\n"
            newspolist = [spo, x[3][0],x[3][1], x[3][2]]
            expand_to_rdfstar(newspolist)
        else:
            clist = [x[3][y:y+2] for y in range(0, len(x[3]),2)]
            for z in clist:
                expand_to_rdfstar([x[0],x[1],x[2],z])
    output = ""
    substitudedict = dict()

    for y in to_remove:
        x = to_remove[y]
        output +=x[0] +" "+ x[1] +" "+ x[2] + "."+"\n"
        expand_to_rdfstar(x)
        if not y in substitudedict:
            substitudedict[y] = output
        output = ""
    print(to_remove)
    for z in substitudedict:
        print("substitudedict", z)
        tree_after = tree_after.replace(z, substitudedict[z])
        print("substitudedict", tree_after)

    output_tree = tree_after

    print("test output tree", output_tree)

    # tree = sparql_lark.parse(output_tree)
    # tt = Process_update().visit(tree)

    return output_tree

def Parsing_and_processing_queries(query):
    global output, annotation_dict,annotation_s_p_o, to_remove, grammar
    sparql_lark = Lark(grammar, start="query", parser="lalr", maybe_placeholders=False)

    from lark import Visitor, v_args
    print("query", query)
    tree = sparql_lark.parse(query)
    print("tree", tree)
    quotation_dict = []
    quotationreif = []
    prefix_dictionary = dict()
    annotation_s_p_o = []
    # to_remove = []
    to_remove = dict()
    annotation_dict = dict()
    output = ""
    def myHash(text:str):
        return str(hashlib.md5(text.encode('utf-8')).hexdigest())
    prefix_replace_list = []

    class Expandanotation(Visitor):
        # output = ""
        global annotation_s_p_o, to_remove, output
        def __init__(self):
            super().__init__()
            self.variable_list = []

        def triplesblock(self, var):

            appends1 = []
            tri = Reconstructorv2(sparql_lark).reconstruct(var)

            if "{|" in tri:

                if len(var.children[0].children) == 2:
                    predicate_object_list2 = var.children[0].children[1]
                    subject = Reconstructorv2(sparql_lark).reconstruct(var.children[0].children[0])
                    po_list = []
                    predicate_objects = predicate_object_list2.children
                    for x in range(0, len(predicate_objects)):

                        predicate_or_object = Reconstructorv2(sparql_lark).reconstruct(predicate_objects[x])
                        po_list.append(predicate_or_object)

                        if len(po_list) == 2:
                            if "," in po_list[1]:
                                po_lists = po_list[1].split(",")

                                for y in po_lists:

                                    try:
                                        object_annotation = y.split("{|",1)
                                        o1 = object_annotation[0]
                                        a1 = "{|"+object_annotation[1]
                                        a1 = a1.strip()
                                        a1_Dict = annotation_dict[a1]
                                        spo_list = [subject,po_list[0],o1, a1_Dict]

                                        annotation_s_p_o.append(spo_list)
                                    except:
                                        spo_list = [subject,po_list[0],y]
                                        annotation_s_p_o.append(spo_list)
                            else:
                                object_annotation = po_list[1].split("{|",1)
                                o1 = object_annotation[0]
                                a1 = "{|"+object_annotation[1]
                                a1_Dict = annotation_dict[a1]
                                spo_list = [subject, po_list[0], o1, a1_Dict]
                                annotation_s_p_o.append(spo_list)
                            po_list = []
                if not tri in to_remove:

                    to_remove[tri] = spo_list


            for x in var.children:
                x1 = Reconstructor(sparql_lark).reconstruct(x)



        def annotationpattern(self, var):
            # print("annotation")
            appends1 = []
            tri2 = Reconstructorv2(sparql_lark).reconstruct(var)

            # print("annotation", tri2)

            for x in var.children[0].children:

                test = Reconstructorv2(sparql_lark).reconstruct(x)
                print("test", test)
                if "{|" in test:
                    test123 = test.split("{|",1)

                    object = test123[0]

                    test123.pop(0)

                    test_annotation = "{|"+ "".join(test123)
                    result = annotation_dict[test_annotation]

                    # if not tri2 in annotation_dict:
                    #     annotation_dict[tri2] = [object,result]
                    # else:
                    #     annotation_dict[tri2].append(object)
                    #     annotation_dict[tri2].append(result)
                    appends1.append(object)
                    appends1.append(result)
                else:
                    # if not tri2 in annotation_dict:
                    #     annotation_dict[tri2] = [test]
                    # else:
                    #     annotation_dict[tri2].append(test)
                    # print("test dict",annotation_dict)
                    appends1.append(test)

            if not tri2 in annotation_dict:
                annotation_dict[tri2] = appends1
            elif not appends1 == annotation_dict[tri2]:
                for x in appends1:
                    annotation_dict[tri2].append(x)

    class ExpandPrefix(Visitor):
        def __init__(self):
            super().__init__()
            # self.quotation_list = []
            self.variable_list = []

        def iri(self, children):
            # print("prefixed_name \n \n\n")
            # pname, = children
            # print("pn", (children.children[0]).children[0])
            prefix_replace_list.append((children.children[0]).children[0])

        def prefixdecl(self, children):
            # print("Sdasd", (children.children))
            vr = Reconstructorv2(sparql_lark).reconstruct(children)
            # print("sadadasd", vr)
            prefix_dictionary[str(children.children[0])] = str(children.children[1])
            # self.children = Tree()
            # self.children.children = self.children
            self = Tree(Token('RULE', 'prefixdecl'), [])

        def base(self, children):
            # print("base")
            base_directive, base_iriref = children
            # print("base", base_directive, base_iriref)
            # Workaround for lalr parser token ambiguity in python 2.7
            if base_directive.startswith('@') and base_directive != '@base':
                raise ValueError('Unexpected @base: ' + base_directive)
    at = ExpandPrefix().visit(tree)
        # print(prefix_dictionary)
    # print()
    sparql = Reconstructorv2(sparql_lark).reconstruct(tree)
    # print("reconstructed tree", sparql, prefix_dictionary)
    for z in prefix_dictionary:
        replace = "PREFIX" + z + prefix_dictionary[z]
        replace1 = "PREFIX" + " "+ z + prefix_dictionary[z]
        replace2 = "PREFIX" + z + " " +prefix_dictionary[z]
        replace3 = "PREFIX" +" "+ z+ " " + prefix_dictionary[z]
        # print(replace)
        # print(sparqlbytes_processing)
        sparql = sparql.replace(replace, "")
        sparql = sparql.replace(replace1, "")
        sparql = sparql.replace(replace2, "")
        sparql = sparql.replace(replace3, "")
        pd = prefix_dictionary[z].strip("<")
        pd = pd.strip(">")
        # sparql = sparql.replace(z, pd)
        for y in prefix_replace_list:
            # print("adsd", y, z, pd)
            if z in y:
                newy = y.replace(z, pd) #repalce y
                newy = "<" + newy + ">"
                # print("newy", newy)
                sparql = sparql.replace(y, newy)
            else:
                pass
    # tree =
    # print("new input", sparql)
    tree = sparql_lark.parse(sparql)
    # print("after", tree)
    tt = Expandanotation().visit(tree)

    tree_after = Reconstructorv2(sparql_lark).reconstruct(tree)
    print("asdasdasdasdas", to_remove, annotation_s_p_o)
    splittree_after = tree_after.split(">")

    PREFIX_substitute = dict()
    for x in splittree_after:

        if "PREFIX" in x:
            y = x + ">"+" " + "\n"
            PREFIX_substitute[x+">"] = y
    for z in PREFIX_substitute:
        tree_after = tree_after.replace(z, "")
    for z in PREFIX_substitute:
        tree_after =  PREFIX_substitute[z] + tree_after


    # for x in to_remove:

    #     x = x + " ."

    #     tree_after = tree_after.replace(x, "")
    # tree_after = tree_after+ "\n" #

    if "PREFIX:" in tree_after:
        tree_after = tree_after.replace("PREFIX:", "PREFIX :")

    def expand_to_rdfstar(x):
        global output
        # print("working", x)
        spo = "<<"+x[0] +" "+x[1] + " " + x[2]+">>"
        # try:
        if len(x[3]) == 2:
            # print("asdadasdasdasd", x[3][0], x[3][1] )

            output += spo + " "+ str(x[3][0]) +" "+str(x[3][1]) + "." + "\n" # smart
            # print("what", output)
        elif len(x[3]) == 3:

            output += spo + " "+ x[3][0] +" "+x[3][1] + "." + "\n" # smart

            newspolist = [spo, x[3][0],x[3][1], x[3][2]]

            expand_to_rdfstar(newspolist)
        else:

            clist = [x[3][y:y+2] for y in range(0, len(x[3]),2)]

            for z in clist:

                expand_to_rdfstar([x[0],x[1],x[2],z])
        # except:
        #     print("error")
        #     pass
    output = ""
    substitudedict = dict()

    for y in to_remove: #yx
        x = to_remove[y]
        # for x in aspo:

        output +=x[0] +" "+ x[1] +" "+ x[2] + "." + "\n"
        expand_to_rdfstar(x)
        # print("addingoutputthis2", output, y)
        if not y in substitudedict:
            substitudedict[y] = output
        output = ""
        #




    for z in substitudedict:
        print("substitudedict", z)
        tree_after = tree_after.replace(z, substitudedict[z])
        print("substitudedict", tree_after)
            # f = lambda L: "{|"+' '.join([f(x) if type(x) is list else x for x in L])+"|}"

            # x1 = f(x)
            # if not x1 in sustitudedict:
            #     sustitudedict[x1] = output

    # print("addingoutputthis", output, sustitudedict)
    output_tree = tree_after
    # if ":G {  }\n" in output_tree:
    #     output_tree = output_tree.replace(":G {  }\n", ":G {")
    #     output_tree = output_tree+ "}"
    # print("test output tree", output_tree[129:])
    print("test output tree", output_tree)

    # print("reer", sparql)
    return output_tree
    # res = g.query("SELECT * { <<:a :b :c>> ?p ?o }")
    # print(list(res))

# import sys # python relative file /document path open
# print(sys.path[0] + '/../../../test/data/sparql-star/sparql-star-annotation-01.rq')
# f = open(sys.path[0] + '/../../../test/data/sparql-star/sparql-star-annotation-01.rq')

# rdbytes = f.read()
# print(rdbytes)
# f.close()
# # bp = rdbytes.decode("utf-8")
# output = Preprocessingqueryintordfstar(rdbytes)
# print("asdasdasd", output)
