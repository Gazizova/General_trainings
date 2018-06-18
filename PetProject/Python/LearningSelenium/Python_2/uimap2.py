# Web Element Locators

class Locators(object):
        LoginDataMap = dict(
                                url ="https://tetra-qa.strikersoft.com/operational",
                                user_login = "tetra-support@strikersoft.com",
                                user_pass= "Qqq!1234",
                                login_button = "//*[@id='loginForm']/button",
                                login_field = "login",
                                password_field = "password")

        DashboardMenuMap = dict(
                                projectTool = "menuButtonAssessmentTool",
                                masterDB = "menuButtonMasterDB",
                                misc = "menuButtonMisc",
                                commonRef = "menuButtonCommonDict",
                                clientRef = "menuButtonClientDict")

        PopsProjectMap = dict(
                                project_code = "record.code",
                                project_note = "record.note",
                                project_address = "record.property.address2",
                                project_client = "record.property.clientName",
                                project_contact = "record.propertyContactDto.name",
                                project_add_button = "actionAdd")
