"""
基础电商客服机器人
功能：模拟电商客服回答用户常见问题
技术栈：Python + OpenAI SDK + 硅基流动API
"""
from openai import OpenAI

# 初始化客户端 - 只需要替换这里的API密钥
client = OpenAI(
    api_key="sk-mxfzpkmbomkgyccfruazplbhkvojwnttvltjofhmpoqwkxge",
    base_url="https://api.siliconflow.cn/v1"
)

# 系统提示词：定义客服角色和行为规范
SYSTEM_PROMPT = """
你是一个专业、热情、有耐心的电商客服，名字叫"小电"。

你的工作规范：
1. 只回答与电商购物相关的问题
2. 回答要简洁明了，不超过3句话
3. 使用亲切的语气，多用"亲"、"哦"、"呢"等语气词
4. 如果不知道答案，就说"亲，这个问题我需要帮您咨询一下仓库哦~"
5. 永远不要和用户争吵，保持友好态度

常见问题标准答案：
- 有运费险吗？：亲，我们家所有产品都有运费险哦，退换货都很方便呢！
- 什么时候发货？：亲，当天下午4点前下单的话，当天就可以发货哦！
- 支持退换货吗？：亲，我们支持7天无理由退换货，质量问题包运费哦！
"""

def chat_with_customer():
    """与用户进行多轮对话"""
    print("=== 电商客服小电 ===")
    print("您好！我是客服小电，有什么可以帮助您的吗？")
    print("输入'退出'结束对话\n")
    
    while True:
        # 获取用户输入
        user_input = input("您：")
        
        # 如果用户输入退出，结束对话
        if user_input.lower() == "退出":
            print("小电：感谢您的咨询，祝您购物愉快！再见~")
            break
        
        # 调用大模型获取回复
        try:
            response = client.chat.completions.create(
                model="Qwen/Qwen2.5-7B-Instruct",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.3,  # 客服场景用较低的温度，保证回答一致
                max_tokens=200
            )
            
            # 打印客服回复
            reply = response.choices[0].message.content
            print(f"小电：{reply}\n")
            
        except Exception as e:
            print(f"小电：不好意思，系统出现了一点问题，请稍后再试哦~")
            print(f"错误信息：{str(e)}\n")

if __name__ == "__main__":
    chat_with_customer()