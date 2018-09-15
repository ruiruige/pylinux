# /usr/bin/env python
# coding=utf-8

import os

from pylinux.common.util.command_util import run_cmd
from pylinux.common.enum.blk_type_enum import FileSystemEnum


class Block(object):
    def __init__(self):
        self.name = None
        self.size = None
        self.type = None
        self.mount_point = None
        self.fs = None
        self.partitions = []

    def is_partition(self):
        return self.type == "part"

    def is_disk(self):
        return self.type == "disk"


def parse_lsblk_output(text):
    """
    to ensure the readability, we do not use a better or best algorithm which is better in performance.

    text example:
    xvda             250G disk
    xvda1   ext4     250G part /
    xvdb    ext4    1000G disk /home/username/name/1.1.1.1
    xvdc    ext4    1000G disk /home/username/name/1.1.1.1/folder_name
    :param text:
    :return:
    """
    block_list = []

    lines = text.split(os.linesep)
    lines = [x.strip() for x in lines]
    lines = [x for x in lines if x]
    for line in lines:
        value_list = line.split(" ")
        value_list = [value for value in value_list if value]

        block = Block()
        block.name = value_list[0]
        block.fs = FileSystemEnum.from_str(value_list[1])
        block.size = value_list[2]
        block.type = value_list[3]
        block.mount_point = None if len(value_list) <= 4 else value_list[5]
        block_list.append(block)

    current_disk = None
    for i, block in enumerate(block_list):
        if block.is_disk():
            current_disk = block
            continue

        if block.is_partition() and current_disk:
            current_disk.partitions.append(block)
            continue

    return block_list


def list_blocks():
    stdout = run_cmd(["sudo", "lsblk", "--output", "NAME,FSTYPE,SIZE,TYPE,MOUNTPOINT", "--noheadings", "--list"],
                     print_command=False)
    block_list = parse_lsblk_output(stdout)
    return block_list
