import json

with open ('text_for_ex7.txt', 'r', encoding = 'utf-8') as f, open("json_for_ex7.json", "w") as json_f:
    firm_dict = {line.split()[0]: float(line.split()[2]) - float(line.split()[3]) for line in f}
    profit_dict = {firm: firm_dict.get(firm) for firm in firm_dict if firm_dict.get(firm) >= 0}
    loss_dict = {firm: -1 * firm_dict.get(firm) for firm in firm_dict if firm_dict.get(firm) < 0}
    average_profit = {'average_profit': sum(profit_dict.values())/len(profit_dict)}
    data_list = [profit_dict, average_profit, loss_dict]
    json.dump(data_list, json_f)