# coding: utf8
from __future__ import unicode_literals

import regex as re

from ..punctuation import ALPHA_LOWER, CURRENCY
from ..tokenizer_exceptions import URL_PATTERN
from ...symbols import ORTH



_exc = {}

for orth in [
    "-e", "A.", "AG.", "AkH.", "Aö.", "B.", "B.CS.", "B.S.", "B.Sc.", "B.ú.é.k.",
    "BE.", "BEK.", "BSC.", "BSc.", "BTK.", "Bat.", "Be.", "Bek.", "Bfok.",
    "Bk.", "Bp.", "Bros.", "Bt.", "Btk.", "Btke.", "Btét.", "C.", "CSC.",
    "Cal.", "Cg.", "Cgf.", "Cgt.", "Cia.", "Co.", "Colo.", "Comp.", "Copr.",
    "Corp.", "Cos.", "Cs.", "Csc.", "Csop.", "Cstv.", "Ctv.", "Ctvr.", "D.",
    "DR.", "Dipl.", "Dr.", "Dsz.", "Dzs.", "E.", "EK.", "EU.", "F.", "Fla.",
    "Folyt.", "Fpk.", "Főszerk.", "G.", "GK.", "GM.", "Gfv.", "Gmk.", "Gr.",
    "Group.", "Gt.", "Gy.", "H.", "HKsz.", "Hmvh.", "I.", "Ifj.", "Inc.",
    "Inform.", "Int.", "J.", "Jr.", "Jv.", "K.", "K.m.f.", "KB.", "KER.",
    "KFT.", "KRT.", "Kb.", "Ker.", "Kft.", "Kg.", "Kht.", "Kkt.", "Kong.",
    "Korm.", "Kr.", "Kr.e.", "Kr.u.", "Krt.", "L.", "LB.", "Llc.", "Ltd.", "M.",
    "M.A.", "M.S.", "M.SC.", "M.Sc.", "MA.", "MH.", "MSC.", "MSc.", "Mass.",
    "Max.", "Mlle.", "Mme.", "Mo.", "Mr.", "Mrs.", "Ms.", "Mt.", "N.", "N.N.",
    "NB.", "NBr.", "Nat.", "No.", "Nr.", "Ny.", "Nyh.", "Nyr.", "Nyrt.", "O.",
    "OJ.", "Op.", "P.", "P.H.", "P.S.", "PH.D.", "PHD.", "PROF.", "Pf.", "Ph.D",
    "PhD.", "Pk.", "Pl.", "Plc.", "Pp.", "Proc.", "Prof.", "Ptk.", "R.", "RT.",
    "Rer.", "Rt.", "S.", "S.B.", "SZOLG.", "Salg.", "Sch.", "Spa.", "St.",
    "Sz.", "SzRt.", "Szerk.", "Szfv.", "Szjt.", "Szolg.", "Szt.", "Sztv.",
    "Szvt.", "Számv.", "T.", "TEL.", "Tel.", "Ty.", "Tyr.", "U.", "Ui.", "Ut.",
    "V.", "VB.", "Vcs.", "Vhr.", "Vht.", "Várm.", "W.", "X.", "X.Y.", "Y.",
    "Z.", "Zrt.", "Zs.", "a.C.", "ac.", "adj.", "adm.", "ag.", "agit.",
    "alez.", "alk.", "all.", "altbgy.", "an.", "ang.", "arch.", "at.", "atc.",
    "aug.", "b.a.", "b.s.", "b.sc.", "bek.", "belker.", "berend.", "biz.",
    "bizt.", "bo.", "bp.", "br.", "bsc.", "bt.", "btk.", "ca.", "cc.", "cca.",
    "cf.", "cif.", "co.", "corp.", "cos.", "cs.", "csc.", "csüt.", "cső.",
    "ctv.", "dbj.", "dd.", "ddr.", "de.", "dec.", "dikt.", "dipl.", "dj.",
    "dk.", "dl.", "dny.", "dolg.", "dr.", "du.", "dzs.", "ea.", "ed.", "eff.",
    "egyh.", "ell.", "elv.", "elvt.", "em.", "eng.", "eny.", "et.", "etc.",
    "ev.", "ezr.", "eü.", "f.h.", "f.é.", "fam.", "fb.", "febr.", "fej.",
    "felv.", "felügy.", "ff.", "ffi.", "fhdgy.", "fil.", "fiz.", "fm.",
    "foglalk.", "ford.", "fp.", "fr.", "frsz.", "fszla.", "fszt.", "ft.",
    "fuv.", "főig.", "főisk.", "főtörm.", "főv.", "gazd.", "gimn.", "gk.",
    "gkv.", "gmk.", "gondn.", "gr.", "grav.", "gy.", "gyak.", "gyártm.", "gör.",
    "hads.", "hallg.", "hdm.", "hdp.", "hds.", "hg.", "hiv.", "hk.", "hm.",
    "ho.", "honv.", "hp.", "hr.", "hrsz.", "hsz.", "ht.", "htb.", "hv.", "hőm.",
    "i.e.", "i.sz.", "id.", "ie.", "ifj.", "ig.", "igh.", "ill.", "imp.",
    "inc.", "ind.", "inform.", "inic.", "int.", "io.", "ip.", "ir.", "irod.",
    "irod.", "isk.", "ism.", "izr.", "iá.", "jan.", "jav.", "jegyz.", "jgmk.",
    "jjv.", "jkv.", "jogh.", "jogt.", "jr.", "jvb.", "júl.", "jún.", "karb.",
    "kat.", "kath.", "kb.", "kcs.", "kd.", "ker.", "kf.", "kft.", "kht.",
    "kir.", "kirend.", "kisip.", "kiv.", "kk.", "kkt.", "klin.", "km.", "korm.",
    "kp.", "krt.", "kt.", "ktsg.", "kult.", "kv.", "kve.", "képv.", "kísérl.",
    "kóth.", "könyvt.", "körz.", "köv.", "közj.", "közl.", "közp.", "közt.",
    "kü.", "lat.", "ld.", "legs.", "lg.", "lgv.", "loc.", "lt.", "ltd.", "ltp.",
    "luth.", "m.a.", "m.s.", "m.sc.", "ma.", "mat.", "max.", "mb.", "med.",
    "megh.", "met.", "mf.", "mfszt.", "min.", "miss.", "mjr.", "mjv.", "mk.",
    "mlle.", "mme.", "mn.", "mozg.", "mr.", "mrs.", "ms.", "msc.", "má.",
    "máj.", "márc.", "mé.", "mélt.", "mü.", "műh.", "műsz.", "műv.", "művez.",
    "nagyker.", "nagys.", "nat.", "nb.", "neg.", "nk.", "no.", "nov.", "nu.",
    "ny.", "nyilv.", "nyrt.", "nyug.", "obj.", "okl.", "okt.", "old.", "olv.",
    "orsz.", "ort.", "ov.", "ovh.", "pf.", "pg.", "ph.d", "ph.d.", "phd.",
    "phil.", "pjt.", "pk.", "pl.", "plb.", "plc.", "pld.", "plur.", "pol.",
    "polg.", "poz.", "pp.", "proc.", "prof.", "prot.", "pság.", "ptk.", "pu.",
    "pü.", "r.k.", "rac.", "rad.", "red.", "ref.", "reg.", "rer.", "rev.",
    "rf.", "rkp.", "rkt.", "rt.", "rtg.", "röv.", "s.b.", "s.k.", "sa.", "sb.",
    "sel.", "sgt.", "sm.", "st.", "stat.", "stb.", "strat.", "stud.", "sz.",
    "szakm.", "szaksz.", "szakszerv.", "szd.", "szds.", "szept.", "szerk.",
    "szf.", "szimf.", "szjt.", "szkv.", "szla.", "szn.", "szolg.", "szt.",
    "szubj.", "szöv.", "szül.", "tanm.", "tb.", "tbk.", "tc.", "techn.",
    "tek.", "tel.", "tf.", "tgk.", "ti.", "tip.", "tisztv.", "titks.", "tk.",
    "tkp.", "tny.", "tp.", "tszf.", "tszk.", "tszkv.", "tv.", "tvr.", "ty.",
    "törv.", "tü.", "ua.", "ui.", "unit.", "uo.", "uv.", "vas.", "vb.", "vegy.",
    "vh.", "vhol.", "vhr.", "vill.", "vizsg.", "vk.", "vkf.", "vkny.", "vm.",
    "vol.", "vs.", "vsz.", "vv.", "vál.", "várm.", "vízv.", "vö.", "zrt.",
    "zs.", "Á.", "Áe.", "Áht.", "É.", "Épt.", "Ész.", "Új-Z.", "ÚjZ.", "Ún.",
    "á.", "ált.", "ápr.", "ásv.", "é.", "ék.", "ény.", "érk.", "évf.", "í.",
    "ó.", "össz.", "ötk.", "özv.", "ú.", "ú.n.", "úm.", "ún.", "út.", "üag.",
    "üd.", "üdv.", "üe.", "ümk.", "ütk.", "üv.", "ű.", "őrgy.", "őrpk.", "őrv."]:
    _exc[orth] = [{ORTH: orth}]


_ord_num_or_date = "([A-Z0-9]+[./-])*(\d+\.?)"
_num = "[+\-]?\d+([,.]\d+)*"
_ops = "[=<>+\-\*/^()÷%²]"
_suffixes = "-[{a}]+".format(a=ALPHA_LOWER)
_numeric_exp = "({n})(({o})({n}))*[%]?".format(n=_num, o=_ops)
_time_exp = "\d+(:\d+)*(\.\d+)?"

_nums = "(({ne})|({t})|({on})|({c}))({s})?".format(
    ne=_numeric_exp, t=_time_exp, on=_ord_num_or_date,
    c=CURRENCY, s=_suffixes)


TOKENIZER_EXCEPTIONS = _exc
TOKEN_MATCH = re.compile("^({u})|({n})$".format(u=URL_PATTERN, n=_nums)).match
