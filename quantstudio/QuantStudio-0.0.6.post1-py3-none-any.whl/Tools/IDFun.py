# coding=utf-8
"""ID的操作函数"""
import re

import numpy as np
import pandas as pd

from QuantStudio import __QS_Error__

# 给A股ID添加后缀
def suffixAShareID(ids):
    if isinstance(ids,str):
        if (ids[0] == '6') or (ids[0] == 'T'):
            return ids+'.SH'
        else:
            return ids+'.SZ'
    else:
        NewIDs = []
        for iID in ids:
            NewIDs.append(suffixAShareID(iID))
        return NewIDs
# 给ID去后缀
def deSuffixID(ids,sep='.'):
    if isinstance(ids,str):
        return ids.split(sep)[0]
    else:
        return [iID.split(sep)[0] for iID in ids]
# 后缀变前缀
def Suffix2Prefix(ids,suffix_sep=".",prefix_sep="_"):
    if isinstance(ids,str):
        Split = ids.split(suffix_sep)
        return Split[-1]+prefix_sep+suffix_sep.join(Split[0:-1])
    else:
        return [Suffix2Prefix(iID) for iID in ids]
# 调整ID序列
def adjustID(ids):
    NewIDs = []
    for jID in ids:
        try:
            jIDStr = str(int(jID))
        except:
            jIDStr = str(jID)
        tempLen = len(jIDStr)
        NewIDs.append('0'*(6-tempLen)+jIDStr)
    return NewIDs
# 测试输入的条件字符串是否有语法错误
def testIDFilterStr(id_filter_str, factor_names=None):
    CompiledIDFilterStr = id_filter_str
    IDFilterFactors = []
    if not factor_names:
        factor_names = re.findall("@(\w+)")
        if "_ID" in factor_names: factor_names.remove("_ID")
    factor_names = sorted(factor_names, key=len, reverse=True)
    for iFactorName in factor_names:
        if CompiledIDFilterStr.find("@"+iFactorName)!=-1:
            CompiledIDFilterStr = CompiledIDFilterStr.replace("@"+iFactorName,"temp['"+iFactorName+"']")
            IDFilterFactors.append(iFactorName)
    CompiledIDFilterStr = CompiledIDFilterStr.replace("@_ID", "temp.index")
    temp = pd.DataFrame(columns=IDFilterFactors)
    try:
        eval("temp["+CompiledIDFilterStr+"]")
    except:
        return (None, None)
    return (CompiledIDFilterStr, IDFilterFactors)
# 过滤 ID
def filterID(factor_data, id_filter_str):
    if not id_filter_str: return factor_data.index.tolist()
    CompiledIDFilterStr, IDFilterFactors = testIDFilterStr(id_filter_str, factor_names=factor_data.columns)
    if CompiledIDFilterStr is None: raise __QS_Error__("ID 过滤字符串有误!")
    temp = factor_data
    return eval("temp["+CompiledIDFilterStr+"].index.tolist()")