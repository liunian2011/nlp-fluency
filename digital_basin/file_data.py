from Xls_resolve import Xls_resolve
import json


def add_result_to_xls(json_obj_param, xls_path):
    json_obj = json.loads(json_obj_param)

    print(f'json object:{json_obj}')
    basin_name = json_obj['Basin_1_Songliao_Basin']['Basic info']['Basin name']
    state = json_obj['Basin_1_Songliao_Basin']['Basic info']['State/Province']
    lat = json_obj['Basin_1_Songliao_Basin']['Basic info']['Latitude']
    long = json_obj['Basin_1_Songliao_Basin']['Basic info']['Longitude']
    locality = json_obj['Basin_1_Songliao_Basin']['Basic info']['Locality Confidence']
    sample = json_obj['Basin_1_Songliao_Basin']['Basic info']['Sample Origin']
    era = json_obj['Basin_1_Songliao_Basin']['Basic info']['Era']
    period = json_obj['Basin_1_Songliao_Basin']['Basic info']['Period']
    strat_unit = json_obj['Basin_1_Songliao_Basin']['Basic info']['Strat Unit']
    well_name = json_obj['Basin_1_Songliao_Basin']['Basic info']['well name']
    well_ori = json_obj['Basin_1_Songliao_Basin']['Basic info']['well orientation']
    type_by_lithology = json_obj['Basin_1_Songliao_Basin']['Source rock type']['Type by Lithology']
    type_by_sedi = json_obj['Basin_1_Songliao_Basin']['Source rock type']['Type by Sedimentary Facies']
    kerogen_type = json_obj['Basin_1_Songliao_Basin']['Kerogen type'][0]
    stage_of_thermal = json_obj['Basin_1_Songliao_Basin']['Stage of thermal maturity for oil generation'][0]
    origin_id = json_obj['Basin_1_Songliao_Basin']['sampling information of the well']['Original ID']
    sample_dep = json_obj['Basin_1_Songliao_Basin']['sampling information of the well']['Sample depth']
    toc = json_obj['Basin_1_Songliao_Basin']['Organic matter richness']['TOC']
    s1 = json_obj['Basin_1_Songliao_Basin']['Organic matter richness']['S1']
    s2 = json_obj['Basin_1_Songliao_Basin']['Organic matter richness']['S2']
    s1s2 = json_obj['Basin_1_Songliao_Basin']['Organic matter richness']['S1+S2']
    s0 = json_obj['Basin_1_Songliao_Basin']['Organic matter richness']['S0']
    s3 = json_obj['Basin_1_Songliao_Basin']['Organic matter richness']['S3']
    vit_ref = json_obj['Basin_1_Songliao_Basin']['Maturity of organic matter']['Vitrinite reflectance (Ro)']
    tmax = json_obj['Basin_1_Songliao_Basin']['Maturity of organic matter']['Tmax']

    print(f'kerogen type:{kerogen_type}')
    resolver = Xls_resolve(xls_path)
    record = ['', '', state, lat, long, locality, basin_name, sample, era, period, strat_unit, well_name, well_ori, origin_id, sample_dep, type_by_lithology, type_by_sedi, toc, s1, s2, s1s2, s0, s3, kerogen_type, vit_ref, tmax, stage_of_thermal]
    print(f'record len:{len(record)}')
    resolver.append_table_data([record])


if __name__ == "__main__":
    json_str = '''
    {
  "Basin_1_Songliao_Basin": {
    "Basic info": {
      "Basin name": "Songliao Basin",
      "State/Province": "The Songliao Basin, located in the central part of Northeast China, belongs to eastern segment of the Xingmeng orogenic belt.",
      "Latitude": "NA",
      "Longitude": "NA",
      "Locality Confidence": "NA",
      "Geographical location": "The studied seven basement metamorphic rocks are located in the southeastern uplift and the western slope of the southern basin.",
      "Sample Origin": "The basement metamorphic rocks in the Songliao Basin mainly consist of metagabbro (L45-1), amphibolite (SN117), metarhyolitical tuff (G190), sericite (Ser) schist (N103), chlorite (Chl) schist (T5-1), biotite (Bi)-actinolite (Act)-quartz (Q) schist (Y205), and metagranite (L44-1).",
      "Era": "Upper Palaeozoic strata are discontinuously distributed in these sub–basins and adjacent areas, which known as the Linxi–Ulanhot stratigraphic area in regional stratigraphic sub–division, and part of upper Palaeozoic strata have subjected to very low–grade (anchizone) metamorphism, such as argillaceous slate in Shoushangou Formation in lower Permian (Wang et al., 2008; Hu et al., 2016).",
      "Period": "Upper Palaeozoic strata are discontinuously distributed in these sub–basins and adjacent areas, which known as the Linxi–Ulanhot stratigraphic area in regional stratigraphic sub–division, and part of upper Palaeozoic strata have subjected to very low–grade (anchizone) metamorphism, such as argillaceous slate in Shoushangou Formation in lower Permian (Wang et al., 2008; Hu et al., 2016).",
      "Strat Unit": "The Permian stratigraphy in western margin of Songliao Basin comprises Shoushangou Formation (SSF, P1ss) and Dashizai Formation (DF, P1d) in lower Permian, Zhesi Formation (ZF, P2z) in middle Permian and Linxi Formation (LF, P3l) in upper Permian (Fig. 2), with a total thickness up to 1.32 km (Wang et al., 2008, 2009, 2009; Chen et al., 2013).",
      "well name": "NA",
      "well orientation": "NA"
    },
    "Source rock type": {
      "Type by Lithology": "NA",
      "Type by Sedimentary Facies": "NA"
    },
    "Kerogen type": ["NA"],
    "Stage of thermal maturity for oil generation": ["NA"],
    "sampling information of the well": {
      "Original ID": "NA",
      "Sample depth": "NA"
    },
    "Organic matter richness": {
      "TOC": "NA",
      "S1": "NA",
      "S2": "NA",
      "S1+S2": "NA",
      "S0": "NA",
      "S3": "NA"
    },
    "Maturity of organic matter": {
      "Vitrinite reflectance (Ro)": "NA",
      "Tmax": "NA"
    }
  }
}
    '''
    xls_path = '/Users/liunian/Downloads/personal/之江实验室/DDE/大模型/DDE数据网络/对接专家/5篇烃源岩数据.xlsx'
    add_result_to_xls(json_str, xls_path)