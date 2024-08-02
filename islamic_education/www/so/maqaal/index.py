import frappe
def get_context(context):
    print("\n\n\n\n\n\n\nn\n\sdffsdfsd")
    print(frappe.form_dict)
    context.blog_detail = frappe.get_doc("Blog Post", frappe.form_dict.title)
    context.blogger = frappe.get_doc("Blogger", context.blog_detail.blogger)
    # get active academic years
    return context
