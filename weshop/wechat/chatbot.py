# -*- coding: utf-8 -*-
from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer

chatbot = ChatBot("MrHippo",
                  read_only=False,  # read_only=False 允许被训练
                  # storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
                  storage_adapter='chatterbot.storage.JsonFileStorageAdapter',  # 注：测试用，数据大时换高效数据库
                  database='./database.json',
                  input_adapter='chatterbot.input.VariableInputTypeAdapter',  # chatterbot.input.TerminalAdapter   chatterbot.input.VariableInputTypeAdapter
                  output_adapter="chatterbot.output.OutputAdapter",  # output_adapter='chatterbot.output.TerminalAdapter',   chatterbot.output.OutputAdapter
                  output_format="text",
                  logic_adapters=[  # 可以自己选择逻辑适配器，模块越多功能越丰富，回复优先级跟输配器顺序有关，按顺序处理，返回分数最高的适配器的回复。
                      {
                          'import_path': 'chatterbot.logic.BestMatch'
                      },
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': '订水',
                          'output_text': '好的，订水网站是xxxx'
                      },
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': '查看锻炼记录',
                          'output_text': '您的锻炼记录是：xxxxx'
                      },
                      # {
                      #     'import_path': 'chatterbot.logic.LowConfidenceAdapter',  # 这个必须放最后，否则很容易匹配到这项。加了这一项貌似不能自我学习
                      #     'threshold': 0.65,
                      #     'default_response': '对不起，我不是很明白.'
                      # }
                      # 'chatterbot.logic.MathematicalEvaluation', # 处理简单的数学问题
                      # 'chatterbot.logic.TimeLogicAdapter' # 处理时间问题
                  ],
                  trainer='chatterbot.trainers.ListTrainer'
                  )


chatbot.train(['最近怎样？', '还不错呢🙂。', '不错不错'])
chatbot.train(['天气怎样？', '快下雨啦😎。', '记得带伞', '好的', '嗯'])


def bot_reply(msg):
    return msg  # str(chatbot.get_response(msg))

if __name__ == '__main__':
    while True:
        try:
            bot_input = chatbot.get_response(None)

        except(KeyboardInterrupt, EOFError, SystemExit):
            break
