escription = 'Verify dashboard contains dropdown option Group by Role can be selected.'

pages = ['dashboard_page']

def test_can_select_by_role(data):
    dashboard_page.navigate()
    click(dashboard_page.dropdown_button)
    click(dashboard_page.group_by_role)
    click(dashboard_page.dropdown_button)
    dashboard_page.check_disabled_dropdown_option("Group by Role")
