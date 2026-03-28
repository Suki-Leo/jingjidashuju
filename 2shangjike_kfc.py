menu = {
    "汉堡": [(15, 7.5), (20, 10)],
    "甜筒": [(8, 7.2), (10, 9)],
    "薯条":[(10, 6), (15, 9)]
}
total_original_price = 0.0  # 非会员总价
total_member_price = 0.0    # 会员总价
for item, prices in menu.items():
    # 打印该商品的规格和价格信息
    print(f"{item} 规格和价格：")
    print(f"  - 中: 原价 ¥{prices[0][0]}, 会员价 ¥{prices[0][1]}")
    print(f"  - 大: 原价 ¥{prices[1][0]}, 会员价 ¥{prices[1][1]}")
    size = input(f"请选择{item}的规格（输入“中”或“大”）：").strip()
    quantity = int(input(f"请输入{item}的购买数量：").strip())
    if size == "中":
        total_original_price += prices[0][0] * quantity
        total_member_price += prices[0][1] * quantity
    elif size == "大":
        total_original_price += prices[1][0] * quantity
        total_member_price += prices[1][1] * quantity
is_member = input("顾客是否为会员？（是/否）：").strip()
if is_member == "是":
    print(f"订单总价是：¥{total_member_price}")
else:
    print(f"订单总价是：¥{total_original_price}")