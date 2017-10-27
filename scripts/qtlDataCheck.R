#
# VERY rough
#

IsVariableOK <- function(varName, varClass, varRequired) {
    # Check if varable is good 
    # 
    #  Example: exists('genome_build')
    #           class(genome_build) == 'character'
    #
    if ((varRequired) && (!exists(varName))) {
        print(paste0('ERROR: ', varName, ' does not exist, but should'))
        return (FALSE)
    } else {
        classesFound <- class(get(varName))
        if (!any(varClass == classesFound)) {            
            print(paste0('ERROR: ', varName, ' is type ', classesFound, ', not ', varClass))
            return (FALSE)
        }
    }
    return (TRUE)
}   
    
CheckVariables <- function() {
    # Check to see if the variables exist and the of the correct type

    # grab the datasets in the environment
    datasets <- grep('^dataset*', apropos('dataset\\.'), value=TRUE)

    if (length(datasets) == 0) {
        print('ERROR: No datasets found')
    }
    
    # expected 
    allNames <- c('genome.build', 'genoprobs', 'K', 'map', 'markers', datasets)
    allClasses <- c('character', 'calc_genoprob', 'list', 'list', 'data.frame', rep('list', length(datasets)))
    allRequired <- c(rep(TRUE, length(allNames)))
    
    # construct the data.frame
    dataCheck <- data.frame(name=allNames, class=allClasses, required=allRequired, stringsAsFactors=FALSE)
    
    # check the variables
    errors <- mapply(IsVariableOK, dataCheck$name, dataCheck$class, dataCheck$required)
}

CheckDatasets <- function(all_vars) {
    # Check to see if the names in each dataset exist and the of the correct class

    # grab the datasets in the environment
    datasets <- grep('^dataset*', apropos('dataset\\.'), value=TRUE)

    # expected elements
    phenoNames <- c('annots', 'covar', 'covar.factors', 'datatype', 'display.name', 'lod.peaks', 'pheno', 'samples')
    phenoClasses <- c('data.frame', 'data.frame', 'data.frame', 'character', 'character', 'data.frame', 'matrix', 'data.frame')
    phenoRequired <- c(TRUE, TRUE, TRUE, TRUE, FALSE, TRUE, TRUE, TRUE)
    
    mrnaNames <- c('annots', 'covar', 'covar.factors', 'datatype', 'display.name', 'ensembl.version', 'expr', 'lod.peaks', 'raw', 'samples')
    mrnaClasses <- c('data.frame', 'data.frame', 'data.frame', 'character', 'character', 'numeric', 'matrix', 'data.frame', 'matrix', 'data.frame')
    mrnaRequired <- c(TRUE, TRUE, TRUE, TRUE, FALSE, FALSE, TRUE, TRUE, FALSE, TRUE)
    
    # construct the data.frame
    dataCheck <- data.frame(name=mrnaNames, class=mrnaClasses, required=mrnaRequired, stringsAsFactors=FALSE)
    
    # be explicit to the end user, we could have used mapply and some trickery, but this is simple
    for (d in datasets) {
        dataset <- get(d)
        
        if (!('datatype' %in% names(dataset))) {
            print(paste0('ERROR: data_type missing for dataset:', d))
            print(paste0('ERROR: Skipping rest of check for dataset:', d))
            next
        }
        
        dataType = dataset[['datatype']]
        
        if (!(dataType %in% c('protein', 'mRNA', 'pheno'))) {
            print(paste0('ERROR: data_type of ', dataType, ' is invalid in dataset: ', d))
            print('ERROR: data_type should be mRNA, protein, or pheno')
            print(paste0('ERROR: Skipping rest of check for dataset: ', d))
            next
        }

        nameList <- phenoNames
        classList <- phenoClasses
        requiredList <- phenoRequired
        
        if (dataType %in% c('protein', 'mRNA')) {
            nameList <- mrnaNames
            classList <- mrnaClasses
            requiredList <- mrnaRequired
        }
            
        # look at the names and classes in the list
        for (n in c(1:length(nameList))) {
            varName <- nameList[n]
            className <- classList[n]
            required <- requiredList[n]
                
            if ((required) && (!(varName %in% names(dataset)))) {
                print(paste0('ERROR: ', varName, ' does not exist in dataset: ', d))
            } else {
                classesFound <- class(dataset[[varName]])
                if (!any(className == classesFound)) {            
                    print(paste0('ERROR: ', varName, ' is type: ', classesFound, ', should be type: ', className, ', in dataset: ', d))
                }
            }
        }
    }
}


CheckExtraVars <- function(allNames) {
    # Check for extra variables
    expectedNames <- c('genome_build', 'genoprobs', 'K', 'map', 'markers',
                       grep('^dataset*', apropos('dataset\\.'), value=TRUE))
    
    extraNames <- setdiff(allNames, expectedNames)
    if (length(extraNames) > 0) {
        print('Warning: the following extra variables were found...')
        print(extraNames)
    }
}


CheckVariables()
CheckDatasets()
#CheckExtraVars(ls())
