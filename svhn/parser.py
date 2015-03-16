import scipy.io
import cPickle
import numpy

def loadmat(filename):
	data=scipy.io.loadmat(filename,struct_as_record=True)
	return data

def convertX(src,begin,end):
	ret=[]
	total=len(src[0][0][0])
	left=int(total*begin)
	right=int(total*end)
	length=right-left
	for i in xrange(length):
		print str(i)+'/'+str(length)+'\r',
		value=[]
		for color in xrange(3):
			for width in xrange(32):
				for height in xrange(32):
					value.append(src[width][height][color][left+i])
		ret.append(numpy.array(value,dtype=numpy.uint8))
	print ''
	return ret

def convertY(src,begin,end):
	ret=[]
	total=len(src)
	left=int(total*begin)
	right=int(total*end)
	length=right-left
	for i in xrange(length):
		print str(i)+'/'+str(length)+'\r',
		ret.append(src[left+i][0]-1)
	return ret

if __name__=='__main__':
	train_mat=loadmat('train_32x32.mat')
	train_size=len(train_mat['y'])
	print 'training set size:'+str(train_size)
	test_mat=loadmat('test_32x32.mat')
	test_size=len(test_mat['y'])
	print 'testing set size:'+str(test_size)

	train_data={}
	validate_data={}
	test_data={}
	train_data['data']=convertX(train_mat['X'],0,1.0)
	train_data['labels']=convertY(train_mat['y'],0,1.0)
	validate_data['data']=convertX(train_mat['X'],0.8,1.0)
	validate_data['labels']=convertY(train_mat['y'],0.8,1.0)
	test_data['data']=convertX(test_mat['X'],0,1.0)
	test_data['labels']=convertY(test_mat['y'],0,1.0)

	train_file=open('train_data','wb')
	validate_file=open('validate_data','wb')
	test_file=open('test_data','wb')
	cPickle.dump(train_data,train_file,protocol=cPickle.HIGHEST_PROTOCOL)
	cPickle.dump(validate_data,validate_file,protocol=cPickle.HIGHEST_PROTOCOL)
	cPickle.dump(test_data,test_file,protocol=cPickle.HIGHEST_PROTOCOL)
