import jpype

from konlpy import jvm


class Morpheme():
    pass

    class Jiana:
        # def __init__(self, dictionary_directory='/root/app/resources/', max_heap_size=1024):
        def __init__(self, dictionary_directory='C:/Apps/DISA3/resources/', max_heap_size=1024):
            jvmpath = jpype.getDefaultJVMPath()

            print(jpype.isJVMStarted())
            if not jpype.isJVMStarted():
                jvm.init_jvm(jvmpath, max_heap_size)

            sentence = "안녕하세요 diquest 어재현입니다. 저는 1988년 3월 28일에 태어났습니다."

            jianaDicPath = dictionary_directory + "jiana/dic/korean/dcd"
            plotDicPath = dictionary_directory + "plot/dic/korean/dcd"
            disaDicPath = dictionary_directory + "disa/dic/korean/dcd"
            category = "SUBWAY_STATION"

            """ step 1 : disa init """
            disaPackage = jpype.JPackage('com.diquest.disa')
            self.jDisa = disaPackage.DISA()
            self.jDisa.init(disaDicPath, plotDicPath, jianaDicPath, category)

        def pos(self, phrase):
            """step 3 : prepare morpheme analyzer tools """
            """step 2 : prepare plotresult & jianaresult """
            self.jDisa.analyze(jpype.java.lang.String(phrase).toCharArray())
            plotPackage = jpype.JPackage('com.diquest.plot')
            jianaPackage = jpype.JPackage('com.diquest.jiana')
            jPlotResult = self.jDisa.getPLOTResult();
            self.jJianaResult = jPlotResult.getJianaResult();

            eoj = self.jJianaResult.getEoj();
            morph = self.jJianaResult.getMorph();
            posTag = self.jJianaResult.getTag();
            eojStart = 0
            eojEnd = 0

            jJianaResultArray = self.jJianaResult.toString().strip().split("\n")

            sentences = phrase.split('\n')
            morphemes = []
            if not sentences:
                return morphemes

            for sentence in sentences:
                for i in range(len(jJianaResultArray)):
                    eojeolList = jJianaResultArray[i].split('\t')[1:]
                    morphemesDict = ()
                    for j in range(len(eojeolList)):
                        keyword = eojeolList[j].split(' ')[0]
                        tag = eojeolList[j].split(' ')[1]
                        morphemesDict = (keyword, tag)
                    morphemes.append(morphemesDict)
            return morphemes

        # def pos(self, phrase):
        #
        #     sentences = phrase.split('\n')
        #     morphemes = []
        #     if not sentences:
        #         return morphemes
        #
        #     for sentence in sentences:
        #         jArray = self.jianaParser.getJianaResultStr(sentence)
        #         morphemes = [(jMap.keySet().iterator().next(), jMap.get(jMap.keySet().iterator().next())) for jMap in jArray]
        #         # morphemes.append(result)
        #     return morphemes
