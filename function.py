
import pandas as pd


def updateVulSavebtn(item, vul, conn):
    cur = conn.cursor()
    i = 0
    for key in item:
        if i < 3:
            cur.execute(
                'Update report_vulnerability set "' + str(key) + '" = "' + str(vul[key]) + '" where "id" = "' + str(
                    item['id']) + '";')
        elif i < 5:
            cur.execute(
                'Update report_cvss2 set "base_score" = "' + str(vul[key]) + '" where "base_score" = "' + str(
                    item['cvss2']) + '";')
        elif i < 6:
            cur.execute(
                'Update report_cvss3 set "base_score" = "' + str(vul[key]) + '" where "base_score" = "' + str(
                    item['cvss3']) + '";')
        else:
            break
        conn.commit()
        item[key] = (vul[key])
        i += 1


def firstLvlTreeGroup(row, all_vul):
    item = {}
    item['Краткое описание'] = 'Будут записи о группах. Нужн подумать какую информацию выводить'
    return item


def firstLvlTree(row, all_vul):
    item = {}
    item['Краткое описание'] = 'Будут записи о узлах, количеств уязмиостей и их среднее значение'

    check = pd.DataFrame.from_dict(all_vul)
    print(check)
    print('check')
    print(check.columns[0])
    print('check')
    print(check.index[0])
    return item


def secondLvlTreeGroup(row, parent_row, all_vul):
    l = 0
    item = {}
    for group in all_vul:
        if l == parent_row:
            item = firstLvlTree(row, all_vul[group])
        l += 1
    return item


def secondLvlTree(row, parent_row, all_vul):
    item = {}
    i = 0
    j = 0
    for key in all_vul:
        if i == parent_row:
            for name in all_vul[key]:
                if j == row:
                    ip_key = key
                    port_name = name
                    break
                j += 1
        i += 1
    item['Количество уязвимостей'] = len(all_vul[ip_key][port_name])
    # print((all_vul[ip_key][port_name]))
    item['Краткое описание'] = 'Будут записи о уязвимостяй в порте и названия протокола'
    return item


def thirdLvlTreeGroup( row, parent_row, parent_parent_row, all_vul):
    l = 0
    item = {}
    for group in all_vul:
        if l == parent_parent_row:
            item = secondLvlTree(row, parent_row, all_vul[group])
        l += 1
    return item


def thirdLvlTree(row, parent_row, parent_parent_row, all_vul):
    i = 0
    j = 0
    k = 0
    item = {}
    for key in all_vul:
        if i == parent_parent_row:
            for name in all_vul[key]:
                if j == parent_row:
                    for vul in all_vul[key][name]:
                        if k == row:
                            item = vul
                            break
                        k += 1
                j += 1

        i += 1

    return item


def fourthLvlTreeGroup(row, parent_row, parent_parent_row, parent_parent_parent_row, all_vul):
    l = 0
    item = {}
    for group in all_vul:
        # print(group)
        if l == parent_parent_parent_row:
            item = thirdLvlTree(row, parent_row, parent_parent_row, all_vul[group])
        l += 1
    return item
