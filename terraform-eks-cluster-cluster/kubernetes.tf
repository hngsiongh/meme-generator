provider "kubernetes" {
  host                   = data.aws_eks_cluster.cluster.endpoint
  token                  = data.aws_eks_cluster_auth.cluster.token
  cluster_ca_certificate = base64decode(data.aws_eks_cluster.cluster.certificate_authority.0.data)
}

/*
  Deploy the Application
*/

resource "kubernetes_namespace" "meme-generator" {
  metadata {
    name = "meme-generator"
  }
}

resource "kubernetes_deployment" "meme-ws" {
  metadata {
    name      = "meme-ws"
    namespace = kubernetes_namespace.meme-generator.metadata.0.name
  }
  spec {
    replicas = 1
    selector {
      match_labels = {
        app = "meme-ws"
      }
    }
    template {
      metadata {
        labels = {
          app = "meme-ws"
        }
      }
      spec {
        container {
          image = "stormaggedon/meme-ws:latest"
          name  = "meme-ws-container"
          port {
            container_port = 8999
          }

          liveness_probe {
            http_get {
              path = "/healthcheck"
              port = 8999

              http_header {
                name  = "X-Custom-Header"
                value = "Awesome"
              }
            }

            initial_delay_seconds = 3
            period_seconds        = 3
          }
        } 
      }
  }
}
}

# Public Facing
resource "kubernetes_service" "meme-ws" {
  metadata {
    name      = "meme-ws"
    namespace = kubernetes_namespace.meme-generator.metadata.0.name
  }
  spec {
    selector = {
      app = kubernetes_deployment.meme-ws.spec.0.template.0.metadata.0.labels.app
    }
    type = "LoadBalancer"
    port {
      port        = 80
      target_port = 8999
    }
  }
}
