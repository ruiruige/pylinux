# /usr/bin/env python
# coding=utf-8


from pylinux.common.searcher.line_setting_searcher import LineSettingSearcher


class RcLocalSearcher(LineSettingSearcher):
    """
    rc.local文件是 line setting文件的一个典型派生情况
    除了最末尾多了一个exit 0
    """



