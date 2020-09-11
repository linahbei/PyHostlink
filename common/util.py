class Util():
    def hex_to_ascii(self, fcs):
        hexstr = "%02X" % fcs
        fcs_high = hexstr[0]
        fcs_low = hexstr[1]
        return fcs_high, fcs_low
        
        
    def assert_fcs(self, frame,  high_7_bit_padding=True):
        buffer = frame.buffer
        buffer_len = len(buffer)
        fcs_high_idx = buffer_len-4
        read_fcs_high = chr(buffer[fcs_high_idx])
        read_fcs_low = chr(buffer[fcs_high_idx+1])
        fcs = 0
        
        for i in range(0, fcs_high_idx):
            fcs = fcs ^ buffer[i]
                        
        if fcs < 0x10 and high_7_bit_padding:
            fcs |= 0x40
            
        fcs_high, fcs_low = self.hex_to_ascii(fcs)
        
        if fcs_high != read_fcs_high or fcs_low != read_fcs_low:
            raise ValueError("FCS not validated. Got char(%s%s), but should be cahr(%s%s)"
                    % (read_fcs_high, read_fcs_low, fcs_high, fcs_low))
        else:
            return
            
    def get_func_name(self, inspect_stack):
        return inspect_stack[0][3]
            