import ast
#ast.literal_eval
f = open('../capture_ok.txt', "r")
data = f.readlines()
def process_data(data):
    process_input = []
    process_output = []
    for dt in data:
        dt_temp = dt.replace("}]},","}]}")
        data_dict=ast.literal_eval(dt_temp)
        Input = data_dict["Inputs"]
        Output = data_dict["Outputs"]
        ##################Process Input#####################
        Head,LeftHand,RightHand=None,None,None
        for i,item in enumerate(Input):
            if item['name'] == "Head":
                posX = float(item["posX"])
                posY = float(item["posY"])
                posZ = float(item["posZ"])
                rotX = float(item["rotX"])
                rotY = float(item["rotY"])
                rotZ = float(item["rotZ"])
                Head = [posX,posY,posZ,rotX,rotY,rotZ]
            if item['name'] == "LeftHand":
                posX = float(item["posX"])
                posY = float(item["posY"])
                posZ = float(item["posZ"])
                rotX = float(item["rotX"])
                rotY = float(item["rotY"])
                rotZ = float(item["rotZ"])
                LeftHand = [posX,posY,posZ,rotX,rotY,rotZ]
            if item['name'] == "RightHand":
                posX = float(item["posX"])
                posY = float(item["posY"])
                posZ = float(item["posZ"])
                rotX = float(item["rotX"])
                rotY = float(item["rotY"])
                rotZ = float(item["rotZ"])
                RightHand = [posX,posY,posZ,rotX,rotY,rotZ]
        general = Head+LeftHand+RightHand
        process_input.append(general)
        #print(process_input)
        ##################End Input#####################

        ##################Process Output#####################
        LeftShoulder,LeftUpperArm,LeftLowerArm,RightShoulder,RightUpperArm,RightLowerArm,Spine=None,None,None,None,None,None,None
        for i,item in enumerate(Output):
            if item['name'] == "LeftShoulder":
                posX = float(item["posX"])
                posY = float(item["posY"])
                posZ = float(item["posZ"])
                rotX = float(item["rotX"])
                rotY = float(item["rotY"])
                rotZ = float(item["rotZ"])
                LeftShoulder = [posX,posY,posZ,rotX,rotY,rotZ]
            if item['name'] == "LeftUpperArm":
                posX = float(item["posX"])
                posY = float(item["posY"])
                posZ = float(item["posZ"])
                rotX = float(item["rotX"])
                rotY = float(item["rotY"])
                rotZ = float(item["rotZ"])
                LeftUpperArm = [posX,posY,posZ,rotX,rotY,rotZ]
            if item['name'] == "LeftLowerArm":
                posX = float(item["posX"])
                posY = float(item["posY"])
                posZ = float(item["posZ"])
                rotX = float(item["rotX"])
                rotY = float(item["rotY"])
                rotZ = float(item["rotZ"])
                LeftLowerArm = [posX,posY,posZ,rotX,rotY,rotZ]
            if item['name'] == "RightShoulder":
                posX = float(item["posX"])
                posY = float(item["posY"])
                posZ = float(item["posZ"])
                rotX = float(item["rotX"])
                rotY = float(item["rotY"])
                rotZ = float(item["rotZ"])
                RightShoulder = [posX,posY,posZ,rotX,rotY,rotZ]
            if item['name'] == "RightUpperArm":
                posX = float(item["posX"])
                posY = float(item["posY"])
                posZ = float(item["posZ"])
                rotX = float(item["rotX"])
                rotY = float(item["rotY"])
                rotZ = float(item["rotZ"])
                RightUpperArm = [posX,posY,posZ,rotX,rotY,rotZ]
            if item['name'] == "RightLowerArm":
                posX = float(item["posX"])
                posY = float(item["posY"])
                posZ = float(item["posZ"])
                rotX = float(item["rotX"])
                rotY = float(item["rotY"])
                rotZ = float(item["rotZ"])
                RightLowerArm = [posX,posY,posZ,rotX,rotY,rotZ]
            if item['name'] == "Spine":
                posX = float(item["posX"])
                posY = float(item["posY"])
                posZ = float(item["posZ"])
                rotX = float(item["rotX"])
                rotY = float(item["rotY"])
                rotZ = float(item["rotZ"])
                Spine = [posX,posY,posZ,rotX,rotY,rotZ]
        general = LeftShoulder+LeftUpperArm+LeftLowerArm+RightShoulder+RightUpperArm+RightLowerArm+Spine
        process_output.append(general)
        #print(process_output)
    return process_input,process_output

#process_input,process_output = process_data(data)
# input_shape = process_input.shape
# output_shape = process_output.shape
#print(input_shape)
#print(len(process_output))