from .consulta_rule import ConsultaRule
from .casaco_rule import CasacoRule
from .default_rule import DefaultRule

def get_rule_by_origem(origem):
    if origem == "consulta":
        return ConsultaRule()
    elif origem == "casaco":
        return CasacoRule()
    return DefaultRule()
