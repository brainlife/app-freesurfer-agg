#!/usr/bin/env python

import csv
import json
import numpy
import glob
import sys
import os

def aggregate(stat):
    for name in stat:
        stat[name] = {'mean': numpy.mean(stat[name]), 'std': numpy.std(stat[name])}

def create_data(stat):
    x = []
    y = []
    error = []
    for name in stat:
        x.append(name)
        y.append(stat[name]['mean'])
        error.append(stat[name]['std'])
    return {
        "type": "bar",
        "x": x,
        "y": y,
        "error_y": {
            "type": "data",
            "array": error,
            "visible": True,
        }
    }

#load values from stats file
with open('config.json') as config_f:
    config = json.load(config_f)

    #aseg.sgtats
    aseg_voxels = {}
    aseg_volume = {}
    aseg_norm_mean = {}
    for output_dir in config["outputs"]:
        stat = open(output_dir+"/stats/aseg.stats")
        for line in stat.readlines():
            if line[0] == "#":
                continue
            values = line.split()
            index = values[0] 
            seg_id = values[1]
            n_voxels = int(values[2])
            volume_mm3 = float(values[3])
            struct_name = values[4]  
            norm_mean = float(values[5])
            norm_stddev = float(values[6])
            norm_min = float(values[7])
            norm_max = float(values[8])
            norm_range = float(values[9])
        
            #print index, struct_name, n_voxels
            if not struct_name in aseg_volume:
                aseg_voxels[struct_name] = []
                aseg_volume[struct_name] = []
                aseg_norm_mean[struct_name] = []
            aseg_voxels[struct_name].append(n_voxels)
            aseg_volume[struct_name].append(volume_mm3)
            aseg_norm_mean[struct_name].append(norm_mean)
    
    aggregate(aseg_voxels)
    aggregate(aseg_volume)
    aggregate(aseg_norm_mean)

    #aparc l
    aparc_l_thick = {}
    aparc_l_gvol = {}
    aparc_l_area = {}
    for output_dir in config["outputs"]:
        stat = open(output_dir+"/stats/lh.aparc.stats")
        for line in stat.readlines():
            if line[0] == "#":
                continue
            values = line.split()
            struct_name = values[0]  
            num_vert = int(values[1])
            surf_area = int(values[2])
            gray_vol = int(values[3])
            thick_avg = float(values[4])
            thick_std = float(values[5])
            mean_curv = float(values[6])
            gaus_curv = float(values[7])
            fold_ind = int(values[8])
            curv_ind = float(values[9])
        
            #print index, struct_name, n_voxels
            if not struct_name in aparc_l_thick:
                aparc_l_thick[struct_name] = []
                aparc_l_gvol[struct_name] = []
                aparc_l_area[struct_name] = []
            aparc_l_thick[struct_name].append(thick_avg)
            aparc_l_gvol[struct_name].append(gray_vol)
            aparc_l_area[struct_name].append(surf_area)

    aggregate(aparc_l_thick)
    aggregate(aparc_l_gvol)
    aggregate(aparc_l_area)

    #aparc r
    aparc_r_thick= {}
    aparc_r_gvol = {}
    aparc_r_area = {}
    for output_dir in config["outputs"]:
        stat = open(output_dir+"/stats/rh.aparc.stats")
        for line in stat.readlines():
            if line[0] == "#":
                continue
            values = line.split()
            struct_name = values[0]  
            num_vert = int(values[1])
            surf_area = int(values[2])
            gray_vol = int(values[3])
            thick_avg = float(values[4])
            thick_std = float(values[5])
            mean_curv = float(values[6])
            gaus_curv = float(values[7])
            fold_ind = int(values[8])
            curv_ind = float(values[9])
        
            #print index, struct_name, n_voxels
            if not struct_name in aparc_r_thick:
                aparc_r_thick[struct_name] = []
                aparc_r_gvol[struct_name] = []
                aparc_r_area[struct_name] = []
            aparc_r_thick[struct_name].append(thick_avg)
            aparc_r_gvol[struct_name].append(gray_vol)
            aparc_r_area[struct_name].append(surf_area)

    aggregate(aparc_r_thick)
    aggregate(aparc_r_gvol)
    aggregate(aparc_r_area)

    #create plots
    plots = []

    data = create_data(aseg_voxels)
    data["name"] = "aseg_voxels";
    plot = {}
    plot["type"] = "plotly"
    plot["name"] = "Aseg Voxels"
    plot["data"] = [data]
    plot["layout"] = {
        "yaxis": {
            "title": "Mean (voxels)",
            #"range": [0, 1],
        },
    }
    plots.append(plot)

    data = create_data(aseg_volume)
    data["name"] = "aseg_volume";
    plot = {}
    plot["type"] = "plotly"
    plot["name"] = "Aseg Volume"
    plot["data"] = [data]
    plot["layout"] = {
        "yaxis": {
            "title": "Mean (mm3)",
        },
    }
    plots.append(plot)

    data = create_data(aseg_norm_mean)
    data["name"] = "aseg_norm_mean";
    plot = {}
    plot["type"] = "plotly"
    plot["name"] = "Aseg Intensity Norm"
    plot["data"] = [data]
    plot["layout"] = {
        "yaxis": {
            "title": "Mean (MR)",
        },
    }
    plots.append(plot)

    data_l = create_data(aparc_l_thick)
    data_l["name"] = "Left";
    data_r = create_data(aparc_r_thick)
    data_r["name"] = "Right";
    plot = {}
    plot["type"] = "plotly"
    plot["name"] = "Aparc Mean Thickness"
    plot["data"] = [data_l, data_r]
    plot["layout"] = {
        "yaxis": {
            "title": "Mean (mm)",
        },
    }
    plots.append(plot)

    data_l = create_data(aparc_l_gvol)
    data_l["name"] = "Left";
    data_r = create_data(aparc_r_gvol)
    data_r["name"] = "Right";
    plot = {}
    plot["type"] = "plotly"
    plot["name"] = "Aparc Gray Matter Volume"
    plot["data"] = [data_l, data_r]
    plot["layout"] = {
        "yaxis": {
            "title": "Mean (mm3)",
        },
    }
    plots.append(plot)

    data_l = create_data(aparc_l_area)
    data_l["name"] = "Left";
    data_r = create_data(aparc_r_area)
    data_r["name"] = "Right";
    plot = {}
    plot["type"] = "plotly"
    plot["name"] = "Aparc Surface Area"
    plot["data"] = [data_l, data_r]
    plot["layout"] = {
        "yaxis": {
            "title": "Mean (mm2)",
        },
    }
    plots.append(plot)

    #write out
    product = {}
    product["brainlife"] = plots
    with open("product.json", "w") as fp:
        json.dump(product, fp)


