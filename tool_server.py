from mcp.server.fastmcp import FastMCP

mcp=FastMCP("tools")

@mcp.tool()
def add_values(value1: float, value2: float) -> str:
    """
    Add two numeric values together.
    
    This tool is useful for basic arithmetic operations in financial calculations,
    such as combining revenue streams, totaling expenses, or summing assets.
    
    Parameters:
    - value1 (float): First numeric value to add
    - value2 (float): Second numeric value to add
    
    Returns:
    - str: The sum of the two values with descriptive text
    
    Example:
    - Adding Q1 revenue ($1.2M) + Q2 revenue ($1.5M) = $2.7M total
    """
    try:
        result = value1 + value2
        return f"Sum: {result:,.2f}"
    except Exception as e:
        return f"Error in addition: {str(e)}"

@mcp.tool()
def subtract_values(value1: float, value2: float) -> str:
    """
    Subtract the second value from the first value.
    
    This tool is commonly used for calculating differences, net values, or changes
    in financial metrics such as profit calculations or variance analysis.
    
    Parameters:
    - value1 (float): Primary value (minuend)
    - value2 (float): Value to subtract (subtrahend)
    
    Returns:
    - str: The difference between the two values with descriptive text
    
    Example:
    - Revenue ($5M) - Expenses ($3M) = $2M profit
    """
    try:
        result = value1 - value2
        return f"Difference: {result:,.2f}"
    except Exception as e:
        return f"Error in subtraction: {str(e)}"

@mcp.tool()
def multiply_values(value1: float, value2: float) -> str:
    """
    Multiply two numeric values together.
    
    This tool is useful for scaling calculations, computing totals based on rates,
    or calculating compound values in financial analysis.
    
    Parameters:
    - value1 (float): First numeric value (multiplicand)
    - value2 (float): Second numeric value (multiplier)
    
    Returns:
    - str: The product of the two values with descriptive text
    
    Example:
    - Units sold (1000) × Price per unit ($25) = $25,000 total revenue
    """
    try:
        result = value1 * value2
        return f"Product: {result:,.2f}"
    except Exception as e:
        return f"Error in multiplication: {str(e)}"

@mcp.tool()
def divide_values(value1: float, value2: float) -> str:
    """
    Divide the first value by the second value.
    
    This tool is essential for calculating ratios, rates, averages, and per-unit
    values in financial analysis and accounting.
    
    Parameters:
    - value1 (float): Dividend (value to be divided)
    - value2 (float): Divisor (value to divide by)
    
    Returns:
    - str: The quotient of the division with descriptive text
    
    Example:
    - Total expenses ($120,000) ÷ Number of months (12) = $10,000 per month
    """
    try:
        if value2 == 0:
            return "Error: Division by zero is not allowed"
        result = value1 / value2
        return f"Quotient: {result:,.2f}"
    except Exception as e:
        return f"Error in division: {str(e)}"

@mcp.tool()
def calculate_revenue_growth(current_revenue: float, previous_revenue: float) -> str:
    """
    Calculate the percentage growth in revenue between two periods.
    
    This tool measures business performance by comparing current period revenue
    to previous period revenue, expressing the change as a percentage.
    
    Parameters:
    - current_revenue (float): Revenue for the current period
    - previous_revenue (float): Revenue for the previous/comparison period
    
    Returns:
    - str: Revenue growth percentage with descriptive text
    
    Formula: ((Current Revenue - Previous Revenue) / Previous Revenue) × 100
    
    Example:
    - Current Q2 revenue: $1.5M, Previous Q1 revenue: $1.2M
    - Growth = ((1.5 - 1.2) / 1.2) × 100 = 25% growth
    """
    try:
        if previous_revenue == 0:
            return "Error: Previous revenue cannot be zero for growth calculation"
        growth = ((current_revenue - previous_revenue) / previous_revenue) * 100
        return f"Revenue Growth: {growth:.2f}%"
    except Exception as e:
        return f"Error in revenue growth calculation: {str(e)}"

@mcp.tool()
def calculate_debt_to_equity_ratio(total_debt: float, total_equity: float) -> str:
    """
    Calculate the debt-to-equity ratio for financial leverage analysis.
    
    This tool measures a company's financial leverage by comparing total debt
    to shareholders' equity. It indicates how much debt a company uses relative
    to equity to finance its operations.
    
    Parameters:
    - total_debt (float): Total debt (short-term + long-term debt)
    - total_equity (float): Total shareholders' equity
    
    Returns:
    - str: Debt-to-equity ratio with descriptive text
    
    Formula: Total Debt ÷ Total Equity
    
    Interpretation:
    - Ratio < 1.0: More equity than debt (conservative)
    - Ratio = 1.0: Equal debt and equity
    - Ratio > 1.0: More debt than equity (aggressive)
    
    Example:
    - Total debt: $500K, Total equity: $1M
    - D/E Ratio = 500K ÷ 1M = 0.50 (conservative leverage)
    """
    try:
        if total_equity == 0:
            return "Error: Total equity cannot be zero for debt-to-equity calculation"
        ratio = total_debt / total_equity
        return f"Debt-to-Equity Ratio: {ratio:.2f}"
    except Exception as e:
        return f"Error in debt-to-equity calculation: {str(e)}"

@mcp.tool()
def calculate_net_profit_margin(net_profit: float, total_revenue: float) -> str:
    """
    Calculate the net profit margin percentage.
    
    This tool measures profitability by showing what percentage of revenue
    remains as profit after all expenses, taxes, and costs are deducted.
    
    Parameters:
    - net_profit (float): Net profit (revenue minus all expenses)
    - total_revenue (float): Total revenue/sales for the period
    
    Returns:
    - str: Net profit margin percentage with descriptive text
    
    Formula: (Net Profit ÷ Total Revenue) × 100
    
    Interpretation:
    - Higher percentages indicate better profitability
    - Industry benchmarks vary significantly
    - Typical ranges: 5-10% (good), 10-20% (excellent), >20% (exceptional)
    
    Example:
    - Net profit: $200K, Total revenue: $1M
    - Net Profit Margin = (200K ÷ 1M) × 100 = 20%
    """
    try:
        if total_revenue == 0:
            return "Error: Total revenue cannot be zero for profit margin calculation"
        margin = (net_profit / total_revenue) * 100
        return f"Net Profit Margin: {margin:.2f}%"
    except Exception as e:
        return f"Error in net profit margin calculation: {str(e)}"

@mcp.tool()
def calculate_roi(gain_from_investment: float, cost_of_investment: float) -> str:
    """
    Calculate the Return on Investment (ROI) percentage.
    
    This tool measures the efficiency of an investment by comparing the gain
    or loss from an investment relative to its cost.
    
    Parameters:
    - gain_from_investment (float): Current value of investment or total return
    - cost_of_investment (float): Original cost/amount invested
    
    Returns:
    - str: ROI percentage with descriptive text
    
    Formula: ((Gain from Investment - Cost of Investment) ÷ Cost of Investment) × 100
    
    Interpretation:
    - Positive ROI: Investment gained value
    - Negative ROI: Investment lost value
    - Higher percentages indicate better investment performance
    
    Example:
    - Investment current value: $120K, Original cost: $100K
    - ROI = ((120K - 100K) ÷ 100K) × 100 = 20%
    """
    try:
        if cost_of_investment == 0:
            return "Error: Cost of investment cannot be zero for ROI calculation"
        roi = ((gain_from_investment - cost_of_investment) / cost_of_investment) * 100
        return f"Return on Investment (ROI): {roi:.2f}%"
    except Exception as e:
        return f"Error in ROI calculation: {str(e)}"
    

if __name__=="__main__":
    mcp.run(transport="streamable-http")