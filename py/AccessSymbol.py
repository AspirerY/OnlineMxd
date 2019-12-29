# -*- coding: utf-8 -*-

import arcpy
import sys,os
reload(sys)
sys.setdefaultencoding( "utf-8" )
os.environ['NLS_LANG'] = 'Simplified Chinese_CHINA.ZHS16GBK'


def access_symbol(mxd_path):
    mxd_doc = arcpy.mapping.MapDocument(mxd_path)
    layer_list = arcpy.mapping.ListLayers(mxd_doc)
    for layer in layer_list:
        layer_name = layer.name
        symbology_type = layer.symbologyType
        print(layer_name)
        print("\n  " + symbology_type)
        if symbology_type == "GRADUATED_COLORS":
            graduated_colors = layer.symbology
            break_descriptions = graduated_colors.classBreakDescriptions
            break_labels = graduated_colors.classBreakLabels
            break_values = graduated_colors.classBreakValues
            break_num = graduated_colors.numClasses
            break_field = graduated_colors.valueField
            print("\n    break_descriptions: " + ", ".join(str(i) for i in break_descriptions))
            print("\n    break_labels: " + ", ".join(str(i) for i in break_labels))
            print("\n    break_values: " + ", ".join(str(i) for i in break_values))
            print("\n    break_num: " + str(break_num))
            print("\n    break_field: " + unicode(str(break_field).encode('utf-8'), encoding='utf-8'))
            print("\n\n")


if __name__ == "__main__":
    mxd_path = sys.argv[1]
    access_symbol(mxd_path)
