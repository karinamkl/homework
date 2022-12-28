
description = 'Verify dashboard contains dropdown with Group by Function and Group by Role options. Group by Function is selected by default. '

pages = ['dashboard_page']


def test_options_in_dropdown(data):
    dashboard_page.navigate()
    wait_for_element_present(dashboard_page.tab_gender)
    click(dashboard_page.dropdown_button)
    assert_element_text(dashboard_page.group_by_function, "Group by Function")
    assert_element_text(dashboard_page.group_by_role, "Group by Role")
    dashboard_page.check_disabled_dropdown_option("Group by Function")
