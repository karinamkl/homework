
description = 'Verify when Grouped by Function and either Race tab is selected, text displayed on page is correct and correct tab is highlighted. '

pages = ['dashboard_page']

def test_by_race(data):
    dashboard_page.navigate()
    wait_for_element_present(dashboard_page.tab_race)
    click(dashboard_page.tab_race)
    dashboard_page.check_active_tab("Race")
    assert_element_text(dashboard_page.pay_equity_gap_label, "Pay Equity Gap")
    assert_element_text(dashboard_page.pay_equity_gap_p, "Hispanics earn 86¢ for every $1 earned by comparable Whites")
    assert_element_text(dashboard_page.employees_comparison_label, "Employees in Comparison")
    assert_element_text(dashboard_page.employees_comparison_p, "Hispanics make up 21% of employees")
    assert_element_text(dashboard_page.budget_label, "Budget")
    assert_element_text(dashboard_page.budget_p, "$535,000 minimum recommended budget to reduce pay equity gap")
