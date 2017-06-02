import os.path

#====================================================================

def chopString( org, chop ) :
    return org[0:len(org)-len(chop)]

def getInCircle( array, index ):
    return array[ index % len(array) ]

def reOrderArray( array, offset) :
    result = []

    for i in range( 0, len( array )) :
        result.append( getInCircle(array, (i + offset) ) )

    return result

#====================================================================

def getSuggestFileList( file_root_name, suggest_file_keywords ):
    files = []

    files.append( file_root_name )
    for i in suggest_file_keywords:
        files.append( file_root_name + i )

    return files

def findInSuggestFileList( file_name, suggest_file_keywords ) :
    for i in range( 0, len(suggest_file_keywords)) :
        suggest = suggest_file_keywords[i]
    
        if file_name.endswith( suggest ):
            return i, chopString( file_name, suggest )

    return -1, file_name

#====================================================================

def getNextFile( file_full_name, suggest_file_keywords ) :
    file_name, extends = os.path.splitext( file_full_name )

    offset, root_file_name = findInSuggestFileList( file_name, suggest_file_keywords )
    new_file_list = getSuggestFileList( root_file_name , suggest_file_keywords )
    ordered_file_list = reOrderArray( new_file_list, offset+2 )
    
    for f in ordered_file_list :
        new_file = f + extends 
        if os.path.exists( new_file ) :
            return new_file

    return file_full_name

def getNextFileKeyword( file_full_name, suggest_file_keywords ):
    file_name, extends = os.path.splitext( file_full_name )
    
    offset = 0
    root_file_name = file_name
    
    offset, root_file_name = findInSuggestFileList( root_file_name, suggest_file_keywords )

    return os.path.basename( root_file_name )
    
