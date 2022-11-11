import logging

def test_loggingdemo():
    # need to create a object
    # this method is help get the logging object
    '''"__name__ - tell which file while showing the error in the log file
    if we are give the "name" it will write as root default'''
    logger = logging.getLogger(__name__)


    # this will show where the file location and name of the file
    filehandler = logging.FileHandler("logfile.log")

    # to handle file format
    '''we are wrapping at in %(asctime) - means it will be evaluated at runtime
    's' - at the end of the bracket so it treats as string so concatenate will happen
    astime - timeformat, levelname - what type of log like error, warning,
    __name__ - name of the file'''
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(__name__)s : %(message)s")
    filehandler.setFormatter(formatter) # connecting the formatter, filehandler to add handler

    '''add handler - used to what format, type of the log file will generate
    It accepts filehandler object to which location the log file need to store
    add handler only print the file'''
    logger.addHandler(filehandler)

    '''set level - to print from the where logs to show. ipo na info la sonna athu print
    from info, warning, error, critical. debug - print panathu
    type of log in Caps'''
    logger.setLevel(logging.INFO)


    '''all type of logs are like print statement only we differentiate for our understanding purpose
    debug, info, warning, error, critical'''

    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    # to print warning
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happened")

    logger.critical("Critical Issue")