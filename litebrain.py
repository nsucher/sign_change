def litebrain(direc, bri):
    # direc is direction from where the light should originate. multiple ok.
    # bri is brightness from 0 (none) to 1 (max)

    if bri > 1:
        bri == 1
    elif bri < 0:
        bri == 0
    else:
        bri == float(bri)

    for j in range(0,len(direc)):
        match direc:
            case 'l':
                v=[270,0]
                psn=[-1,0,0]
                return v, psn
            case 'r': #right
                v=[90,0]
                psn=[1,0,0]
                return v, psn
            case 'a': #anterior
                v=[180,0]
                psn=[0,1,0]
                return v,psn
            case 'p': #posterior
                v=[0,0]
                psn=[0,-1,0],
            case 's': #superior
                v=[0,90]
                psn=[0,0,1]
                return v, psn
            case 'i': #inferior
                v=[180,-90]
                psn=[0,0,-1]
                return v, psn
            case 'd': #diagonal (antero-superior)
                v=[0,-90]
                psn=[0,0,-1]
                return v, psn
        V[j,:] = v
        P[j,:] = psn
    # merges to a single angle for both, in case multiple entered
    V = np.mean(V,1)
    P = np.mean(P,1)

    # apply
    #TODO: 3d plot -- where to place?

    # if direc == 'i':
    #     # view(V(1), V(2))
    #     # plt.axes(projection='3d').view_init()
    # else:
    #     view(P)
    #
    # if bri:
    #     set(light,'position',P,'color',bri*[1 1 1])

