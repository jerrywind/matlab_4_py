def rat(x, tol=None, isRel=False, isReturnSeq=False):
    """
    Using continuous fractions with a tolerance, result close to matlab rat function,
    use numpy to add precision

    e.g:
      pi = 3.14.......
      rat(pi, isReturnSeg=True)[-1] == [3, 7, 16]
      rat(pi, tol = 1e-7, isReturnSeg=True)[-1] == [3, 7, 16, -294]

    :param x: input float
    :param tol: tolerance
    :param isRel: True for tolerance is relevent scale, False for absolute tolerance
    :param isReturnSeq: need to return continuous faction number sequence or not (first element is the Integer part)
    :return: numerator, denomerator, appoxFloat, [continuous faction number sequence] if isReturnSeq
    """

    x = np.float64(x)
    if tol is None:
        tol = x * 1e-6
    elif isRel:
        tol = x * np.float64(tol)
    else:
        tol = np.float64(tol)
    # init
    m00, m01, m10, m11 = np.float64(1), np.float64(0), np.float64(0), np.float64(1)
    numer, denom = x , np.float64(1.0)
    contSeq, residual = [], x
    while True:
        intCeil = np.ceil(residual)
        intFloor = np.floor(residual)
        if intCeil == intFloor:
            break
        residualCeil = np.float64(1.0) / (residual - intCeil)
        residualFloor = np.float64(1.0) / (residual - intFloor)
        if np.abs(residualCeil) < np.abs(residualFloor):
            residual, contiInt = residualFloor, intFloor
        else:
            residual, contiInt = residualCeil, intCeil
        contSeq.append(contiInt)

        tmp = m00 * contiInt + m01
        m01 = m00
        m00 = tmp
        tmp = m10 * contiInt + m11
        m11 = m10
        m10 = tmp

        if np.abs(x - (m00 / m10)) < tol:
            numer, denom = m00, m10
            break
    ret = [numer, denom, np.divide(m00, m10)]
    if isReturnSeq:
        ret.append(contSeq)
    return ret
    
    
    
    
    
def gcd(x, y):
    a,b = deepcopy(x),deepcopy(y)
    while b!=0:
        b2 = b
        a, b = b2, a % b2
    return a
