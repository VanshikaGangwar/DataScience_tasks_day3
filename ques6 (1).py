import pandas as pd
df = pd.read_csv("employee_performance.csv")

print("Dataset Preview:")
print(df.head())

exceptional_performers = df[df["Score"] > 90]
print("\nExceptional Performers:")
print(exceptional_performers)


sales_department = df[df["Department"] == "Sales"]
print("\nSales Department Records:")
print(sales_department)


sorted_by_score = df.sort_values(by="Score", ascending=False)
print("\nEmployees Ranked by Score:")
print(sorted_by_score)

sorted_dept_score = df.sort_values(by=["Department", "Score"], ascending=[True, False])
print("\nDepartment-wise Rankings:")
print(sorted_dept_score)

avg_score_dept = df.groupby("Department")["Score"].mean().reset_index()
print("\nAverage Score per Department:")
print(avg_score_dept)

max_score_quarter = df.groupby("Quarter")["Score"].max().reset_index()
print("\nMaximum Score per Quarter:")
print(max_score_quarter)

print("\n✅ Analysis Complete")
