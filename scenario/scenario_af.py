import json
from consts.consts import BASE_REVISION
from scenario.scenario import Scenario
from consts.consts_af import AF_STUDY_TAG, CONFIG_MAP, AF_STUDY_MODE, VCB_CONFIG, VCBB_CONFIG


class ArcFlashScenario(Scenario):
    """
    The ArcFlashScenario class is responsible for creating arc flash study scenarios
    within the ETAP environment. It extends the base Scenario class to include specific
    configurations and scenarios related to arc flash studies.
    """

    def __init__(self, url: str, revisions: list[str] | None = None):
        """
        Initializes an ArcFlashScenario instance with the specified ETAP connection port.

        :param str url: local URL for connecting to ETAP datahub.
        :param list[str] | None revisions: List of revisions to be included in arc flash scenario creation.

        Revisions rules:
            1. All revisions - revisions = None
            2. Base revision - revisions = []
            3. Only some revisions - revisions = [...]
        """
        super().__init__(url)
        self.revisions = revisions

    def create_scenarios(self) -> None:
        """
        Creates arc flash study scenarios by iterating over combinations of electrode configurations,
        switching configurations, and revision configurations. Each scenario is uniquely identified
        by a combination of the study case, switching configuration, and revision configuration.

        The generated scenarios are added to the ETAP project and the scenarios XML file is updated.

        - Electrode configurations: VCB (Vacuum Circuit Breaker) and VCBB (Vacuum Circuit Breaker Box).
        - Switching configurations: Derived from the ETAP project configurations, excluding 'Ultimate'.
        - Revisions: Derived from the ETAP project revisions.
        """
        # Retrieve switching configurations and remove the 'Ultimate' configuration
        all_revisions = json.loads(self.etap.projectdata.getrevisions())
        switching_configs = json.loads(self.etap.projectdata.getconfigurations())
        if self.revisions is None:
            self.revisions = all_revisions
        if isinstance(self.revisions, list):
            self.revisions = [rev for rev in self.revisions if rev in all_revisions]
            if not self.revisions:
                self.revisions = [BASE_REVISION]

        if 'Ultimate' in switching_configs:
            switching_configs.remove('Ultimate')
        if 'ULT' in switching_configs:
            switching_configs.remove('ULT')

        # Define electrode configurations for arc flash studies
        electrode_configs = [VCB_CONFIG, VCBB_CONFIG]

        # Iterate over electrode, switching, and revision configurations to create scenarios
        for electrode_config in electrode_configs:
            for switching_config in switching_configs:
                for revision in self.revisions:
                    # Construct the study case name and scenario identifier
                    study_case = AF_STUDY_TAG + '_' + electrode_config
                    rev_config_name = ('_' + revision) if revision != BASE_REVISION else ''
                    switching_config_name = CONFIG_MAP.get(switching_config, switching_config)
                    scenario_id = study_case + '_' + switching_config_name + rev_config_name

                    # Create the scenario and add its ID to the list
                    self.create_scenario(scenario_id, switching_config, AF_STUDY_MODE, study_case,
                                         revision, scenario_id)
                    self.scenario_ids.append(scenario_id)

        # Write the updated scenarios to the XML file
        self.write_scenario_xml()
