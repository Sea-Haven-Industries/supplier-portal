app_name = "suppliers_portal"
app_title = "Suppliers Portal"
app_publisher = "jeowsome15@gmail.com"
app_description = "Supplier Invoices, Supplier Quotes and Supplier Details"
app_email = "jeowsome15@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "suppliers_portal",
# 		"logo": "/assets/suppliers_portal/logo.png",
# 		"title": "Suppliers Portal",
# 		"route": "/suppliers_portal",
# 		"has_permission": "suppliers_portal.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/suppliers_portal/css/suppliers_portal.css"
# app_include_js = "/assets/suppliers_portal/js/suppliers_portal.js"

# include js, css files in header of web template
# web_include_css = "/assets/suppliers_portal/css/suppliers_portal.css"
# web_include_js = "/assets/suppliers_portal/js/suppliers_portal.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "suppliers_portal/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "suppliers_portal/public/seahaven.svg"

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
# 	"methods": "suppliers_portal.utils.jinja_methods",
# 	"filters": "suppliers_portal.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "suppliers_portal.install.before_install"
# after_install = "suppliers_portal.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "suppliers_portal.uninstall.before_uninstall"
# after_uninstall = "suppliers_portal.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "suppliers_portal.utils.before_app_install"
# after_app_install = "suppliers_portal.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "suppliers_portal.utils.before_app_uninstall"
# after_app_uninstall = "suppliers_portal.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "suppliers_portal.notifications.get_notification_config"

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

doc_events = {
	"Supplier": {
		"autoname": "suppliers_portal.overrides.supplier.generate_supplier_id",
		"after_insert": "suppliers_portal.overrides.supplier.create_user",
	}
}

# Scheduled Tasks
# ---------------

scheduler_events = {
	# 	"all": [
	# 		"suppliers_portal.tasks.all"
	# 	],
	# 	"daily": [
	# 		"suppliers_portal.tasks.daily"
	# 	],
	# 	"hourly": [
	# 		"suppliers_portal.tasks.hourly"
	# 	],
	# 	"weekly": [
	# 		"suppliers_portal.tasks.weekly"
	# 	],
	# 	"monthly": [
	# 		"suppliers_portal.tasks.monthly"
	# 	],
}

# Testing
# -------

# before_tests = "suppliers_portal.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "suppliers_portal.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "suppliers_portal.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["suppliers_portal.utils.before_request"]
# after_request = ["suppliers_portal.utils.after_request"]

# Job Events
# ----------
# before_job = ["suppliers_portal.utils.before_job"]
# after_job = ["suppliers_portal.utils.after_job"]

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
# 	"suppliers_portal.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


website_route_rules = [
	{"from_route": "/supplier-portal/<path:app_path>", "to_route": "supplier-portal"},
	{"from_route": "/erpnext", "to_route": "/app"},
]

export_python_type_annotations = True

jinja = {
	"methods": [
		"suppliers_portal.overrides.print.amount_in_words_with_asterisks",
	]
}
