import frappe

def get_context(context):
    # Set the base_template_path to None to render without Frappe's default UI
    context.no_cache = 1
    context.show_sidebar = False
    context.base_template_path = None
    
    # This tells Frappe to render the HTML file as-is without wrapping it in the framework
    return context
