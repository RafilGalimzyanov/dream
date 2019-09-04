from typing import List, Tuple

from deeppavlov.core.common.registry import register
from deeppavlov.core.models.component import Component
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


@register('rule_based_selector')
class RuleBasedSelector(Component):
    """
    Rule-based skill selector which choosing among TransferTransfo, Base AIML and Alice AIML
    """
    wh_words = {"what", "when", "where", "which", "who", "whom", "whose", "why"}

    def __init__(self, **kwargs):
        logger.info("Skill selector Initialized")
        pass

    def __call__(self, states_batch, **kwargs) -> List[List[str]]:

        skill_names = []

        for dialog in states_batch:
            skills_for_uttr = []

            tokens = dialog['utterances'][-1]['text'].lower().split()

            if "/new_persona" in dialog['utterances'][-1]['text']:
                skills_for_uttr.append("personality_catcher")  # TODO: rm crutch of personality_catcher
            elif len(set(tokens).intersection(self.wh_words)) > 0:
                skills_for_uttr.append("cobotqa")
                skills_for_uttr.append("program_y")
                skills_for_uttr.append("transfertransfo")
            else:
                skills_for_uttr.append("program_y")
                skills_for_uttr.append("transfertransfo")

            skill_names.append(skills_for_uttr)

        return skill_names
