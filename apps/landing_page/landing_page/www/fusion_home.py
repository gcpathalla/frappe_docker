import frappe

def get_context(context):
    # Disable Frappe's default UI wrapper completely
    context.no_cache = 1
    context.show_sidebar = False
    
    # Critical: Set base_template_path to None to render raw HTML
    context.base_template_path = None
    
    return context
