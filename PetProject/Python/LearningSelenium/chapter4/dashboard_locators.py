import unittest


class Locators(object):


    server_url = "https://tetra-qa.strikersoft.com/operational"

#
    projectTool ="menuButtonAssessmentTool"
    masterDB = "menuButtonMasterDB"
    misc = "menuButtonMisc"
    commonRef = "menuButtonCommonDict"
    clientRef = "menuButtonClientDict"

    # SECOND LEVEL PROJECT MENU IN POPS
    CREATE_PROJECT =      "menuButtonCreateAssessment"

    # SECOND LEVEL MASTER_DB MENU IN POPS
    MASTER_DB_CLIENTS =            "menuButtonMasterDBClients"
    MASTER_DB_PROPERTIES    =       "menuButtonMasterDBProperties"

    # SECOND LEVEL MISC MENU IN POPS
    MISC_USERS_MENU                 =   "menuButtonMiscUsers"
    MISC_GROUPS_MENU                =     "menuButtonMiscGroups"
    MISC_SYNC_PROJECT_MENU =   "menuButtonMiscAlphatrackerSynchronize"
    MISC_CLIENT_DATA_IMPORT_MENU =          "menuButtonMiscClientDataImport"

    # SECOND LEVEL COMMON_REFERENCES POPUP MENU IN POPS
    COMMON_REFERENCES_AOC_MENU   =                       "commonDict1"
    COMMON_REFERENCES_ENFORCEMENT_VISIT_CATEGORY_MENU =  "commonDict2"
    COMMON_REFERENCES_PROPERTY_USAGE_MENU   =           "commonDict3"
    COMMON_REFERENCES_TASK_GROUP_MENU  =                 "commonDict4"
    COMMON_REFERENCES_TASK_STATUS_MENU    =              "commonDict5"
    COMMON_REFERENCES_TASK_INTERVAL_MENU    =            "commonDict6"
    COMMON_REFERENCES_TASK_REPOSITORY_MENU   =           "commonDict7"
    COMMON_REFERENCES_ACTION_STATUS_MENU       =         "commonDict8"
    COMMON_REFERENCES_ROLES_MENU            =            "commonDict9"
    COMMON_REFERENCES_LIBRARY_MENU              =        "commonDict10"
    COMMON_REFERENCES_ACCIDENT_CATEGORY_MENU      =      "commonDict11"
    COMMON_REFERENCES_PEOPLE_INTERVIEWED_STATUS_MENU=    "commonDict12"
    COMMON_REFERENCES_ROLE_IN_INCIDENT_MENU           =  "commonDict13"
    COMMON_REFERENCES_EMAIL_NOTIFICATION_CONFIG_MENU   = "commonDict14"

# POPS Dashboard
    search_ref =  "refNum"

# Create Project
    project_code = "record.code"
    project_note = "record.note"
    project_address = "record.property.address2"
    project_client = "record.property.clientName"
    project_contact = "record.propertyContactDto.name"
    project_add_button = "actionAdd"

# JSS stage
