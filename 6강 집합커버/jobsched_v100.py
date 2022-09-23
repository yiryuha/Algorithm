###########################################
#####   제목 : 작업 스케쥴링 그리디 알고리즘
#####   작성자: 김성훈
#####   작성일: 2017.04.19
###########################################

def findWorkableMachine(S, t):
    def is_overlap(t1, t2):
        if t1[0] < t2[0]:
            if t1[1] > t2[0] :
                #  이 조건에서는 다음과 같은 상황일때, 겹침
                #   t1[0]---------t1[1]
                #            t2[0]-------------t2[1]  
                #   t1[0]--------------------------t1[1]
                #            t2[0]-------------t2[1]  
                return True
            else :
                #  이 조건에서는 다음과 같은 상황일때, 겹치지 않음.
                #   t1[0]------t1[1]
                #                   t2[0]------t2[1]  
                return False
        else :
            if t1[0] < t2[1] : 
                #  이 조건에서는 다음과 같은 상황일때, 겹침
                #          t1[0]--------------t1[1]
                #   t2[0]-------------t2[1]  
                #          t1[0]--------t1[1]
                #   t2[0]-------------------t2[1]  
                return True
            else :
                #  이 조건에서는 다음과 같은 상황일때, 겹치지 않음.
                #                   t1[0]--------t1[1]
                #   t2[0]------t2[1]  
                
                return False            
        
    for m_id in range(len(S)):
        workable = True
        jobList = S[m_id]
        for ti in jobList:
            if is_overlap(t[1], ti[1]) :
##                print("Overlap: ", ti, t)
                workable = False 
                break
        if workable :
            return m_id
    return None

def jobScheduling(L):
##입력: n개의 작업 t1, t2, ⋯, tn
##출력: 각 기계에 배정된 작업 순서
    # t1, 1개작업의 표현: (작업명, 작업시간) --> ('t1', (1,5)) 
    # L,작업 리스트: (('t1', (1, 5)), ('t2', (3, 7)),....)
    # return S: 기계별 배정 작업리스트
    #   S --> 작업 리스트의 리스트: ((('t1',...),('t5',...)),....)      
##
    S = []
    # 아래 라인은 테스트 목적의 임시코드임. 코드 작성시에 삭제바람. 
    #S.append(T)
    
##1. 시작시간의 오름차순으로 정렬한 작업 리스트: L
    #TODO TODO
    L= list(L)
    L.sort(key=lambda t: t[1][0])

##2. while ( L ≠∅ ) {
    #TODO
    while( len(L) > 0 ) :
##3.      L에서 가장 이른 시작시간 작업 ti를 가져온다.
        #TODO
        t = L.pop(0)
##4.    if (ti를 수행할 기계가 있으면)
        #TODO TODO
        m_id = findWorkableMachine(S, t)
        if m_id is not None :
##5.        ti를 수행할 수 있는 기계에 배정한다.
            #TODO
            S[m_id].append(t)
##6.    else
        #TODO
        else:
##7.        새로운 기계에 ti를 배정한다.
            #TODO TODO
            newMachineJobList = list()
            newMachineJobList.append(t)
##8.        ti를 L에서 제거한다.
            #TODO
            S.append( newMachineJobList )
##     }
##9. return 각 기계에 배정된 작업 순서
    #TODO
    return S



if __name__=='__main__':
    t1 = ('t1', (7,8))
    t2 = ('t2', (3,7))
    t3 = ('t3', (1,5))
    t4 = ('t4', (5,9))
    t5 = ('t5', (0,2))
    t6 = ('t6', (6,8))
    t7 = ('t7', (1,6))
    
    L = (t1, t2, t3, t4, t5, t6, t7)
    for t in L : print (t)
    mJobSched = jobScheduling(L)
    i = 1
    for mJob in mJobSched:
        print ("M%02d:%s"%(i, mJob))
        i = i+1
