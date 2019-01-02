

비어게임으로 본 생산/분배 전략


노희태, 범길원, 박진우, 채성욱
산업경영공학과
인천대학교

------------------------------------------------------------------------------------
1. 첫 번째 시도(개별전략)
•	첫 번째 시도는 소매상, 도매상, 분배센터, 공장이 각각 개별적인 전략을 갖고 게임을 시행한다.
•	협업(정보교환)은 없는 것으로 한다.

1.	전략개요
o	50 Game Data Set을 매크로를 통해 추출한다.
o	추출한 데이터를 주기성을 고려한 지수평활법(ETS, Winter’s Model)을 통해 수요를 예측한다.
o	예측데이터의 95% 신뢰상한을 구한다. 이는 백로그 발생 시 발생하는 비용이 재고가 누적되는 비용보다 경제적이지 못하기 때문이다.
o	이를 기준으로 엑셀 해찾기를 활용하여 공급망 내 의사결정자들의 주문량과 생산량을 결정한다.
o	각 의사결정자들은 위 수치를 토대로 정보교환 없이 데이터를 입력하여 게임을 진행한다.
 
 
 
 
 
 

2.	게임결과
소매상을 제외한 의사결정자들은 JIT방식을 사용하여 최초재고를 소진 시킨 후 재고와 백로그를 0으로 유지할 수 있다. 그러나 소매상의 경우에는 최초재고 소진 후에 수요 예측값과 실 수요의 차이로 인해 재고가 계속 누적되었다. 그 결과 총 비용 또한 선형적으로 증가하는 채찍효과를 확인 할 수 있다. 따라서, 우리는 JIT방식을 유지하며 소매상의 재고수준을 최소한으로 낮추어 총 비용을 혁신적으로 낮출 수 있는 알고리즘을 고안하였다.




2. 두 번째 시도(협업전략)
•	두 번째 시도는 소매상, 도매상, 분배센터, 공장이 협업하여 게임을 시행한다.
•	수요량, 재고량 등 모든 정보의 교환, 열람이 가능하다.

1.	전략개요
o	각 공급망 단계 간의 리드타임이 2주이므로 JIT를 유지한 채 즉시 생산자의 생산량을 조절하면 6주 뒤에 소매상에게 전달 된다.
o	따라서 위의 정보를 토대로 다음과 같은 알고리즘을 개발, 이용하여 실시간으로 정보를 교환하며 주문량과 생산량을 유연하게 조정하였다.



2.	게임결과
첫 번째 시도와 같이 소매상을 제외한 의사결정자들은 JIT방식을 유지하며 최초재고를 소진 시킨 후 재고와 백로그를 0으로 유지할 수 있었다. 소매상의 재고가 10이상이 될 경우, 실시간으로 전체 공급망에 정보를 전달하여 JIT 방식을 유지함과 동시에 소매상의 누적된 재고를 소모 시키며 일정하게 유지 시킬 수 있었다. 그 결과 첫 번째 시도보다 획기적인 비용절감을 이루어 낼 수 있었다.



3. 결론 및  추후 연구 과제
본 연구에서는 공급사슬에서 발생하는 채찍효과를 최소화하는 방법을  제시하였다. 그 결과 정량적인 요소 중에는 공급망에서 정확한 수요예측과 리드타임의 측정이 중요하는 것을 볼 수 있었다.

또한 정성적인 요소 중에는 실시간 데이터를 모든 공급망에 공유하는 것이 가장 중요함을 알 수 있었다. 데이터가 공유되지 않으면 실시간 정보를 알 수 가 없고, 각 공급망이 이기심을 누르고 전체 공급망의 최소비용을 위해 노력하지 않으면 JIT 시스템도 유지 될 수 없다.

따라서 최대한 많은 빅데이터를 축적하고, 여러가지 수요예측 기법을 비교, 활용하여 정확한 수요예측을 하고, 물자 이동의 리드타임을 표준화 하며, 실시간으로 모든 공급망의 정보를 공유할 경우 JIT 시스템을 유지하고 전체 공급망의 효율성을 높일 수 있다.

본 연구에서 제시된 엑셀 해찾기와, 알고리즘은 사례연구에서 볼 수 있듯이 실제 기업 현장에서도 적용할 수 있으며 이를 통해 공급망 내부의 주체들을 설득하는 지표로도 활용 할 수 있을 것이다. 

추후 연구과제로는 본 연구에서 진행한 상황 외에 천재지변, 환율상승, 법적규제와 같은 예측 불가능한 불확실성을 고려하는 상황에 따른 채찍효과의 측정과 그것을 해결하는 모델링 또한 필요할 것이다.

5. 참고 문헌
1.	국내 물류기업의 SCM 지원역량 강화방안 연구(2014. 12  한국로직스틱스학회)
