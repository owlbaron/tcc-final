from vision.contexts.context import Context
from vision.contexts.fight_attack_menu import FightAttackMenuContext
from vision.contexts.fight_main_menu import FightMainMenuContext
from vision.contexts.yes_no_menu import YesNoMenuContext
from vision.object import Object
from enum import Enum
from typing import Iterable, List, TypeVar

T = TypeVar("T")

#https://www.delenamalan.co.za/til/2020-11-13-sorting-a-list-by-priority-in-python.html#final-solution
def sort_by_priority_list(values: Iterable[T], priority: List[int]) -> List[T]:
    """
    Sorts an iterable according to a list of priority items.
    Usage:
    >>> sort_by_priority_list(values=[1,2,2,3], priority=[2,3,1])
    [2, 2, 3, 1]
    >>> sort_by_priority_list(values=set([1,2,3]), priority=[2,3])
    [2, 3, 1]
    """
    priority_dict = {k: i for i, k in enumerate(priority)}
    def priority_getter(obj):
        return priority_dict.get(obj.get_class_id(), len(values))
    return sorted(values, key=priority_getter)


class ClassIDs(Enum):
    ATTACK_CHANGE_MENU = 0
    BAG_MENU = 1
    BATTLE = 2
    EXPLORATION = 3
    FIGHT_ATTACK_MENU = 4
    FIGHT_BAG_MENU = 5
    FIGHT_MAIN_MENU = 6
    INDICATOR = 7
    MAP = 8
    MENU = 9
    POKE_CENTER_MENU = 10
    POKEMON_SELECTION = 11
    YES_NO_MENU = 12

PRIORIDADE = [
    ClassIDs.YES_NO_MENU.value,
    ClassIDs.ATTACK_CHANGE_MENU.value,
    ClassIDs.POKEMON_SELECTION.value,
    ClassIDs.POKE_CENTER_MENU.value,
    ClassIDs.BAG_MENU.value, 
    ClassIDs.MENU.value,
    ClassIDs.FIGHT_ATTACK_MENU.value,
    ClassIDs.FIGHT_BAG_MENU.value,
    ClassIDs.FIGHT_MAIN_MENU.value,
    ClassIDs.MAP.value,
    ClassIDs.BATTLE.value, 
    ClassIDs.EXPLORATION.value,
    ClassIDs.INDICATOR.value
]

class ContextFactory:
    """
    Padrão de projeto de Factory para gerar os diferentes contextos.
    """
    def create(self, objects: list[Object]) -> Context:
        """
        Gera o contexto atual, será gerado o com maior prioridade.

        Exemplo:
            - [FightMainMenu, YesNoMenu] -> YesNoMenu
            Pois o contexto de menu vem por cima de tudo para confirmar algo,
            logo, tem maior prioridade.

        Parâmetros:
            - objects: a lista de objetos reconhecidos pelo modelo.

        Retorno:
            - Context: o Contexto com maior prioridade.
        """
        print("--- ContextFactory ---")
        print(f"# objetos encontrados: {len(objects)}")
        print(f"objetos: {objects}")
        if len(objects) != 0:
            objects_sorted = sort_by_priority_list(objects, PRIORIDADE)
            print(f"objetos ordenados por prioridade: {objects_sorted}")
            main_object: Object = objects_sorted[0]
            class_id = main_object.get_class_id()
            print(f"class id do principal: {class_id}")
            last_object: Object =  objects_sorted[-1]
            indicator = last_object if last_object.get_class_id() == ClassIDs.INDICATOR.value else None


            d: dict[int, Context] = {
                ClassIDs.FIGHT_MAIN_MENU.value: FightMainMenuContext(indicator),
                ClassIDs.FIGHT_ATTACK_MENU.value: FightAttackMenuContext(indicator),
                ClassIDs.YES_NO_MENU.value: YesNoMenuContext(indicator),
            }

            if class_id in d.keys():
                return d[class_id]
                
        return Context()
