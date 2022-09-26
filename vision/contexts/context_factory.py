from vision.contexts.context import Context
from vision.contexts.fight_attack_menu import FightAttackMenuContext
from vision.contexts.fight_main_menu import FightMainMenuContext
from vision.contexts.yes_no_menu import YesNoMenuContext
from vision.object import Object
from enum import Enum
from typing import Iterable, List, TypeVar

T = TypeVar("T")

#https://www.delenamalan.co.za/til/2020-11-13-sorting-a-list-by-priority-in-python.html#final-solution
def sort_by_priority_list(values: Iterable[T], priority: List[T]) -> List[T]:
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


class class_ids(Enum):
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

# Pensar na prioridade de menus/objetos
PRIORIDADE = [1, 2]

class ContextFactory:
    """TODO"""
    def create(self, objects: list[Object]) -> Context:
        """TODO"""
        objects_sorted = sort_by_priority_list(objects, PRIORIDADE)
        main_object: Object = objects_sorted[0]
        class_id = main_object.get_class_id()

        d = {
            class_ids.FIGHT_MAIN_MENU: FightMainMenuContext(),
            class_ids.FIGHT_ATTACK_MENU: FightAttackMenuContext(),
            class_ids.YES_NO_MENU: YesNoMenuContext(),
        }

        if class_id in d:
            return d[class_id]

        return Context()
