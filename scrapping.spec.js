describe('WebScrape', function () {

	beforeEach(function () {
			cy.visit('https://www.instagram.com/direct/t/111590610236036/')
	})

	it('Scrape Data', function () {
			cy.get('#dtDGrid>tbody>tr.DataRow')
			.each(function($row, index, $rows){

					cy.wrap($row).within(function(){
							cy.get('td')
							.each(function($cellData, index, $columns){
									cy.log($cellData.text())
							}
							)
					}
					)
			}
			)
	})