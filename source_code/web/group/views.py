from django.shortcuts import render

# Create your views here.

from pandas.tests.io.excel.test_xlrd import xlrd
from werkzeug.utils import secure_filename, redirect
from flask import Blueprint, render_template, request, url_for
from app.controller import teacher

fileBP = Blueprint('file',__name__)
UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'data')

global studentList
studentList = []

@fileBP.route('/import',methods=['GET','POST'])
def Update_file():
    if request.method == 'GET':
        #print(session.get('teacher_email'))
        return render_template('Import.html',title='Sample Import',header='Test import',teacher = teacher)
    else:
        avatar = request.files.get('avatar')
        # 对文件名进行包装，为了安全,不过对中文的文件名显示有问题
        filename = secure_filename(avatar.filename)
        avatar.save(os.path.join(UPLOAD_PATH, filename))
        #read file
        read_path = UPLOAD_PATH + '\\' + filename
        workbook = xlrd.open_workbook(read_path)
        Data = workbook.sheets()[0]
        row = Data.nrows
        col = Data.ncols
        for i in range(row):
            rowlist = []
            for j in range (col):
                # append all in list
                rowlist.append(Data.cell_value(i,j))
            #add to the list
            studentList.append(rowlist)
        del studentList[0]#delete first row

        return redirect(url_for('teacher.GetAcc',teacher = teacher))