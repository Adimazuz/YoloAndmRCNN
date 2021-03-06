import subprocess

from combCNN import CombinedNet as my_net
from MAPCalculator import MAPCalculator
import cnn_utils
from cnn_utils import div2sets

import os
from our_paths import *

calc = MAPCalculator()
# combinedNet = my_net()
result_dict = {}
for i, chosen_pic in enumerate(os.listdir(pics_path)):
    if i<6000:
        continue
    if i==7000: #7000
        break

    print("start pic %s " % chosen_pic + " i= " + str(i))

    if os.path.exists(os.path.join(ground_truth_test_path, str(calc.imageNameToId(chosen_pic)) + '.txt')):
        continue

    real_box = calc.getGroundTruth(chosen_pic)
    cnn_utils.savePredictionsToFile(ground_truth_test_path, str(calc.imageNameToId(chosen_pic)) + '.txt', real_box)

    # combinedNet.readImage(pics_path + chosen_pic)
    # try:
    #     combinedNet.predict()
    # except:
    #     print("exception %s", i)
    #     os.remove(os.path.join(ground_truth_path, str(calc.imageNameToId(chosen_pic)) + '.txt'))
    #     continue
    # result_dict = {}
    # result_dict["res_ByHighestScoreTakeAllIou80"] = combinedNet.filterByHighestScoreTakeAll(0.8)
    # result_dict["res_ByHighestScoreTakeAllIou70"] = combinedNet.filterByHighestScoreTakeAll(0.7)
    # result_dict["res_ByHighestScoreTakeAllIou60"] = combinedNet.filterByHighestScoreTakeAll(0.6)
    # result_dict["res_ByHighestScoreTakeAllIou50"] = combinedNet.filterByHighestScoreTakeAll(0.5)
    # result_dict["res_ByHighestScoreTakeWithConf90"] = combinedNet.filterByHighestScoreTakeWithConf(0.7, 0.90)
    # result_dict["res_ByHighestScoreTakeWithConf80"] = combinedNet.filterByHighestScoreTakeWithConf(0.7, 0.80)
    # result_dict["res_ByHighestScoreTakeWithConf70"] = combinedNet.filterByHighestScoreTakeWithConf(0.7, 0.70)
    # result_dict["res_yolo_only"] = combinedNet.getYoloRes()
    # result_dict["res_mrnn_only"] = combinedNet.getMrcnnRess()
    #
    # for kye, ress in result_dict.items():
    #     cnn_utils.savePredictionsToFile(prediction_test_path + str(kye), str(calc.imageNameToId(chosen_pic)) + '.txt',
    #                                     ress)

    # combinedNet.show(res)
    print("finished pic %s" % chosen_pic)

coco = 7



# map_output_path = "/home/dima/YoloAndmRCNN/map_output/map.txt"
# for kye in result_dict:
#     cmd = 'python ' + calc_map_script_path + ' -np -q --ground_true_path ' + ground_truth_path + ' --predict_path ' + prediction_test_path + str(
#         kye)
#     # TODO convert map to class or copy to our env.
#     proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
#                             stderr=subprocess.PIPE, shell=True)
#     # koko = proc.communicate()[0]
#     with open(map_output_path, 'a+') as filehandle:
#         filehandle.write("map of: " + str(kye) + " is:\n" + str(proc.communicate()[0]) + " \n\n")
#
# coco = 1
