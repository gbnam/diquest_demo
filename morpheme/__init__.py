# import pickle
# from konlpy.tag import *
# from os import path
# import h5py
# import pandas
#
# # def decrator_function(load_object):
# #     def wrapper_function(*args):
# #         morpheme_type = *args
# #         print(type(*args)," : ",*args, ' : 2')
# #         if morpheme_type == 'mecab':
# #             morpheme_object = Okt()
# #         elif morpheme_type == 'okt':
# #             morpheme_object = Okt()
# #         elif morpheme_type == 'komoran':
# #             morpheme_object = Komoran()
# #         elif morpheme_type == 'hannanum':
# #             morpheme_object = Hannanum()
# #         elif morpheme_type == 'kkma':
# #             morpheme_object = Kkma()
# #         elif morpheme_type == 'jiana':
# #             # morpheme_object = Jiana()
# #             morpheme_object = Okt()
# #         return load_object(*args)
# #
# #     return wrapper_function
#
#
# # @decrator_function
# def load_object(file_name):
#     file_path = "{}.hdf5".format(file_name)
#     print(file_path)
#     if not path.exists(file_path):
#         # object_file = h5py.File(file_path, "w")
#         object_file = open(file_path, "wb")
#         morpheme_object = None
#         if file_name == 'mecab':
#             morpheme_object = Okt()
#         elif file_name == 'okt':
#             morpheme_object = Okt()
#         elif file_name == 'komoran':
#             morpheme_object = Komoran()
#         elif file_name == 'hannanum':
#             morpheme_object = Hannanum()
#         elif file_name == 'kkma':
#             morpheme_object = Kkma()
#         elif file_name == 'jiana':
#             # morpheme_object = Jiana()
#             morpheme_object = Okt()
#
#         # object_file.create_dataset('morpheme', (morpheme_object))
#         # object_file.close()
#
#         pickle.dump(morpheme_object, object_file)
#
#     # object_file = h5py.File(file_path, "r")
#     # List all groups
#     # print("Keys: %s" % object_file.keys())
#     # a_group_key = list(object_file.keys())[0]
#
#     # Get the data
#     # data = list(object_file[a_group_key])
#     # stored_object = pickle.load(object_file)
#     # data = {}
#     return ''
#
#
# a = load_object('mecab')
# print(a)
