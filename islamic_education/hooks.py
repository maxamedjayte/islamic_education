app_name = "islamic_education"
app_title = "Islamic Education"
app_publisher = "Maxamed Jayte"
app_description = "this full-islamic education with has students classes attendce hr "
app_email = "maxamedltc@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/islamic_education/css/islamic_education.css"
# app_include_js = "/assets/islamic_education/js/islamic_education.js"

# include js, css files in header of web template
# web_include_css = "/assets/islamic_education/css/islamic_education.css"
# web_include_js = "/assets/islamic_education/js/islamic_education.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "islamic_education/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "islamic_education.utils.jinja_methods",
# 	"filters": "islamic_education.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "islamic_education.install.before_install"
# after_install = "islamic_education.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "islamic_education.uninstall.before_uninstall"
# after_uninstall = "islamic_education.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "islamic_education.utils.before_app_install"
# after_app_install = "islamic_education.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "islamic_education.utils.before_app_uninstall"
# after_app_uninstall = "islamic_education.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "islamic_education.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"islamic_education.tasks.all"
# 	],
# 	"daily": [
# 		"islamic_education.tasks.daily"
# 	],
# 	"hourly": [
# 		"islamic_education.tasks.hourly"
# 	],
# 	"weekly": [
# 		"islamic_education.tasks.weekly"
# 	],
# 	"monthly": [
# 		"islamic_education.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "islamic_education.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "islamic_education.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "islamic_education.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["islamic_education.utils.before_request"]
# after_request = ["islamic_education.utils.after_request"]

# Job Events
# ----------
# before_job = ["islamic_education.utils.before_job"]
# after_job = ["islamic_education.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"islamic_education.auth.validate"
# ]

website_route_rules = [
    # student
    {"from_route": "/fr/report/student/detail/<name>", "to_route": "fr/report/student/detail"},

    # attend
    {"from_route": "/fr/attending-week/<name>", "to_route": "fr/attending-week"},
    {"from_route": "/fr/print/attending-week/<attend_week>/<classe>","to_route":"fr/print/attending-week/"},

    # blog post
    {"from_route": "/so/maqaal/<title>", "to_route": "so/maqaal/"},


    # 

]