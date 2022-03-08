def solution(id_list, report, k):
    report_dict = {}
    mail_dict = {}
    
    for i in id_list :
        report_dict.setdefault( i, [] )
        mail_dict.setdefault( i, 0 ) 

    for i in report :
        report_dict[ i.split(' ')[1] ].append( i.split(' ')[0] )
        report_dict[ i.split(' ')[1] ] = list( set( report_dict[ i.split(' ')[1] ] ) )
          
    for i in report_dict.items() :
        if len( i[1] ) >= k :
            for j in i[1] : mail_dict[ j ] += 1
    
    return list(mail_dict.values())
