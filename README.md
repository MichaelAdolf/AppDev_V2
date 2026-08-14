repo.save(
27
HistoricalSetupEntry(
28
symbol=symbol,
29
 
30
setup_date=(
31
f"2025-{(i % 12)+1:02d}-01"
32
),
33
 
34
entry_price=100 + i,
35
 
36
target_pct=0.08,
37
 
38
success=i % 3 != 0,
39
 
40
days_to_target=randint(
41
5,
42
60
43
),
44
 
45
max_gain_pct=uniform(
46
5.0,
47
25.0
48
),
49
 
50
max_drawdown_pct=uniform(
51
-15.0,
52
0.0
53
)
54
)
55
)
56
 
57
count += 1
