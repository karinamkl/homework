
description = 'Verify when Grouped by Role and either Gender tab is selected, text displayed on page is correct and correct tab is highlighted. '

pages = ['dashboard_page']


def test_by_gender(data):
    dashboard_page.navigate()
    click(dashboard_page.dropdown_button)
    click(dashboard_page.group_by_role)
    wait_for_element_present(dashboard_page.tab_gender)
    dashboard_page.check_active_tab("Gender")
    assert_element_text(dashboard_page.pay_equity_gap_label, "Pay Equity Gap")
    assert_element_text(dashboard_page.pay_equity_gap_p, "Men earn 97¢ for every $1 earned by comparable Women")
    assert_element_text(dashboard_page.employees_comparison_label, "Employees in Comparison")
    assert_element_text(dashboard_page.employees_comparison_p, "Men make up 47% of employees")
    assert_element_text(dashboard_page.budget_label, "Budget")
    assert_element_text(dashboard_page.budget_p, "$135,000 minimum recommended budget to reduce pay equity gap")
