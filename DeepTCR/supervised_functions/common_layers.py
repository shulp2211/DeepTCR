import tensorflow as tf

def Get_Gene_Features(self,embedding_dim_genes,gene_features):
    if self.use_v_beta is True:
        X_v_beta = tf.placeholder(tf.int64, shape=[None, ], name='Input_V_Beta')
        X_v_beta_OH = tf.one_hot(X_v_beta, depth=len(self.lb_v_beta.classes_))
        embedding_layer_v_beta = tf.get_variable(name='Embedding_V_beta',
                                                 shape=[len(self.lb_v_beta.classes_), embedding_dim_genes])
        X_v_beta_embed = tf.matmul(X_v_beta_OH, embedding_layer_v_beta)
        gene_features.append(X_v_beta_embed)
    else:
        X_v_beta = None
        X_v_beta_OH = None
        embedding_layer_v_beta = None

    if self.use_d_beta is True:
        X_d_beta = tf.placeholder(tf.int64, shape=[None, ], name='Input_D_Beta')
        X_d_beta_OH = tf.one_hot(X_d_beta, depth=len(self.lb_d_beta.classes_))
        embedding_layer_d_beta = tf.get_variable(name='Embedding_D_beta',
                                                 shape=[len(self.lb_d_beta.classes_), embedding_dim_genes])
        X_d_beta_embed = tf.matmul(X_d_beta_OH, embedding_layer_d_beta)
        gene_features.append(X_d_beta_embed)
    else:
        X_d_beta = None
        X_d_beta_OH = None
        embedding_layer_d_beta = None

    if self.use_j_beta is True:
        X_j_beta = tf.placeholder(tf.int64, shape=[None, ], name='Input_J_Beta')
        X_j_beta_OH = tf.one_hot(X_j_beta, depth=len(self.lb_j_beta.classes_))
        embedding_layer_j_beta = tf.get_variable(name='Embedding_J_Beta',
                                                 shape=[len(self.lb_j_beta.classes_), embedding_dim_genes])
        X_j_beta_embed = tf.matmul(X_j_beta_OH, embedding_layer_j_beta)
        gene_features.append(X_j_beta_embed)
    else:
        X_j_beta = None
        X_j_beta_OH = None
        embedding_layer_j_beta = None

    if self.use_v_alpha is True:
        X_v_alpha = tf.placeholder(tf.int64, shape=[None, ], name='Input_V_Alpha')
        X_v_alpha_OH = tf.one_hot(X_v_alpha, depth=len(self.lb_v_alpha.classes_))
        embedding_layer_v_alpha = tf.get_variable(name='Embedding_V_Alpha',
                                                 shape=[len(self.lb_v_alpha.classes_), embedding_dim_genes])
        X_v_alpha_embed = tf.matmul(X_v_alpha_OH, embedding_layer_v_alpha)
        gene_features.append(X_v_alpha_embed)
    else:
        X_v_alpha = None
        X_v_alpha_OH = None
        embedding_layer_v_alpha = None

    if self.use_j_alpha is True:
        X_j_alpha = tf.placeholder(tf.int64, shape=[None, ], name='Input_J_Alpha')
        X_j_alpha_OH = tf.one_hot(X_j_alpha, depth=len(self.lb_j_alpha.classes_))
        embedding_layer_j_alpha = tf.get_variable(name='Embedding_J_Alpha',
                                                 shape=[len(self.lb_j_alpha.classes_), embedding_dim_genes])
        X_j_alpha_embed = tf.matmul(X_j_alpha_OH, embedding_layer_j_alpha)
        gene_features.append(X_j_alpha_embed)
    else:
        X_j_alpha = None
        X_j_alpha_OH = None
        embedding_layer_j_alpha = None

    if gene_features:
        gene_features = tf.concat(gene_features, axis=1)

    return X_v_beta, X_v_beta_OH, embedding_layer_v_beta,\
            X_d_beta, X_d_beta_OH, embedding_layer_d_beta,\
            X_j_beta, X_j_beta_OH, embedding_layer_j_beta,\
            X_v_alpha,X_v_alpha_OH,embedding_layer_v_alpha,\
            X_j_alpha,X_j_alpha_OH,embedding_layer_j_alpha,\
            gene_features

def Get_Ortho_Loss(x,alpha=1e-3):
    x_norm = tf.nn.l2_normalize(x, 0)
    loss = alpha * tf.reduce_sum(tf.multiply(x_norm, x_norm))
    return loss

def Get_Ortho_Loss_dep(x,alpha=1e-4):
    loss = tf.abs(tf.matmul(x,x,transpose_b=True) - tf.eye(tf.shape(x)[-2]))
    loss = alpha*tf.reduce_sum(loss)
    return loss

