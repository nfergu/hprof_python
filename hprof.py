from typing import BinaryIO, Any, List


class HProfWriter:

    def __init__(self, file: BinaryIO):
        self._file = file

    def write_instance(self, obj: Any, stack_trace_serial_num: int, class_object_id: int,
                       referrents: List[Any]):
        """
        INSTANCE DUMP (0x21)

        ID: object ID
        u4: stack trace serial number
        ID: class object ID
        u4: number of bytes that follow
        [value]*: instance field values (this class, followed by super class, etc)
        """
        self._write_u1(0x21)
        #TODO: Add rest of record incl size etc
        self._write_id(id(obj))
        self._write_u4(stack_trace_serial_num)
        self._write_id(class_object_id)

    def _write_id(self, identifier: int):
        self._file.write(identifier.to_bytes(length=4))

    def _write_u1(self, u1: int):
        self._file.write(bytes([u1]))

    def _write_u4(self, u4: int):
        self._file.write(u4.to_bytes(length=4))