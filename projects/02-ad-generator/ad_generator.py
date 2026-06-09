"""
电商广告语生成器
功能：根据商品名称和品类，生成3条不同风格的广告语
技术栈：Python + OpenAI SDK + 硅基流动API + DeepSeek-V3模型
"""
from openai import OpenAI
import datetime

# 初始化DeepSeek客户端（硅基流动兼容OpenAI接口）
client = OpenAI(
    # 替换为你自己的硅基流动API密钥
    api_key="sk-mxfzpkmbomkgyccfruazplbhkvojwnttvltjofhmpoqwkxge",
    base_url="https://api.siliconflow.cn/v1"
)

# 系统提示词：明确要求生成3种不同风格的广告语
SYSTEM_PROMPT = """
你是一个专业的电商文案策划师。
根据用户提供的商品名称和品类，生成3条不同风格的广告语。

要求：
1. 第一条：活泼可爱风，适合小红书、抖音
2. 第二条：专业品质风，适合京东、天猫详情页
3. 第三条：限时促销风，适合直播间、朋友圈
4. 每条广告语不超过20个字
5. 格式清晰，每条前面标清楚风格
6. 不要有多余的解释和说明

输出格式示例：
【活泼风】夏日必备！清爽透气不闷热
【专业风】优质面料，匠心工艺，品质之选
【促销风】限时特惠！买一送一，错过再等一年
"""

def generate_advertisements():
    """生成广告语并保存到文件"""
    print("=== 电商广告语生成器 ===")
    
    # 获取用户输入
    product_name = input("请输入商品名称：")
    product_category = input("请输入商品品类：")
    print("\n正在生成广告语，请稍候...\n")
    
    try:
        # 调用DeepSeek API
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3",  # 使用DeepSeek-V3模型
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"商品名称：{product_name}\n商品品类：{product_category}"}
            ],
            temperature=0.8,  # 文案生成用稍高的温度，增加多样性
            max_tokens=300
        )
        
        # 获取生成结果
        ad_content = response.choices[0].message.content
        
        # 打印结果
        print("生成成功！以下是为您生成的广告语：\n")
        print(ad_content)
        
        # 保存到TXT文件
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{product_name}_广告语_{timestamp}.txt"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"商品名称：{product_name}\n")
            f.write(f"商品品类：{product_category}\n")
            f.write(f"生成时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(ad_content)
        
        print(f"\n✅ 广告语已保存到文件：{filename}")
        
    except Exception as e:
        print(f"\n❌ 生成失败：{str(e)}")
        print("请检查API密钥是否正确，网络是否正常。")

if __name__ == "__main__":
    generate_advertisements()