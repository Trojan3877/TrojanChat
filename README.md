![Uploading image.png…]()


# TrojanChat 🚀

![Capstone](https://img.shields.io/badge/Capstone-Complete-brightgreen.svg)
![Built By](https://img.shields.io/badge/Built%20By-Trojan3877-blue.svg)
![Mobile CI](https://github.com/Trojan3877/TrojanChat/actions/workflows/mobile-ci.yml/badge.svg?branch=main)
![CI](https://github.com/Trojan3877/TrojanChat/actions/workflows/ci.yml/badge.svg?branch=main)
![CodeQL](https://github.com/Trojan3877/TrojanChat/actions/workflows/codeql.yml/badge.svg?branch=main)
![DVC](https://img.shields.io/badge/DVC-enabled-blue)
![Docker](https://img.shields.io/docker/pulls/trojan3877/trojanchat-service)
![Kubernetes](https://img.shields.io/badge/Kubernetes-ready-green)
![Helm](https://img.shields.io/badge/Helm–Chart-orange)
![Ansible](https://img.shields.io/badge/Ansible-automated-yellowgreen)
![License](https://img.shields.io/badge/license-MIT-green)

**TrojanChat** is **my baby**—a real-time chat platform for USC fans, built entirely from my own idea and code. This project showcases:

1. **Cross-Platform Mobile**  
   - Android & iOS with React Native  
   - 🚀 Fastlane + GitHub Actions mobile CI  

2. **Scalable Backend**  
   - Go microservice (Gorilla Mux + Firebase)  
   - Dockerized & deployable via Kubernetes + Helm  

3. **Analytics & Monitoring**  
   - Google Analytics & Firebase Analytics integration  
   - Prometheus + Grafana dashboards  

4. **DevOps Automation**  
   - DVC data/versioning  
   - GitHub Actions CI/CD (lint, test, build, deploy)  
   - Ansible for infra configuration  
   - Terraform for cloud provisioning  

5. **Polished UX & Governance**  
   - Interactive Dashboard with Chart.js  
   - CHANGELOG, CONTRIBUTING, SECURITY, CODEOWNERS  

---

## Quickstart

```bash
git clone https://github.com/Trojan3877/TrojanChat.git
cd TrojanChat

# Local setup
cp .env.example .env 
scripts/setup_local.sh

# Run backend & frontend
docker-compose up -d

# K8s deploy (dev)
kubectl apply -f k8s/
helm upgrade --install trojanchat helm/trojanchat

# Full prod deploy
make deploy









